import datetime
import os
import sys
from jsonschema import validate
from unittest import TestCase, skip
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.util.event import EventLogs
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.tasks import MonitorSiemLogs
from komand_mimecast.tasks.monitor_siem_logs.schema import MonitorSiemLogsOutput
from util import Util, FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, SIEM_LOGS_HEADERS_RESPONSE


@patch("requests.request", side_effect=Util.mocked_request)
class TestMonitorSiemLogs(TestCase):
    def setUp(self) -> None:
        self.task = Util.default_connector(MonitorSiemLogs())

    def test_monitor_siem_logs_success(self, _mock_data):
        content = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2]
        token = SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token")
        tests = [
            {"next_token": "happy_token", "resp": content, "has_more_pages": True, "token": token},
            {"next_token": "force_json_error", "resp": content, "has_more_pages": True, "token": token},
            {"next_token": "no_results", "resp": [], "has_more_pages": False, "token": "no_results"},
        ]
        for test in tests:
            with self.subTest(f"Success test with token: {test.get('next_token')}"):
                test_state = {"next_token": test.get("next_token")}
                response, new_state, has_more_pages, status_code, _ = self.task.run(params={}, state=test_state)

                self.assertEqual(has_more_pages, test.get("has_more_pages"))
                self.assertEqual(response, test.get("resp"))
                self.assertEqual(new_state, {"next_token": test.get("token")})
                self.assertEqual(status_code, 200)
                validate(response, MonitorSiemLogsOutput.schema)

    @skip("Have not pulled logic to raise 401 successfully - TODO in 5.3.6")
    def test_monitor_siem_logs_raises_401(self, _mock_data):
        # TODO: update 401 logic to successfully check is_last_token that was introduced in 5.3.3
        state_params = {"next_token": "force_401"}

        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)

        self.assertEqual(status_code, 401)
        self.assertEqual(response, [])
        self.assertEqual(new_state, state_params)  # we shouldn't change the state if we encounter an error
        self.assertEqual(type(error), ApiClientException)

    @skip("Have pulled the sanitise method as possible negative seek cause - TODO in 5.3.6")
    @patch("logging.Logger.error")
    def test_monitor_siem_logs_stops_path_traversal(self, mock_logger, _mock_data):
        test_state = {"next_token": "path_traversal"}  # this forces our mock util to append `../` into filenames
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching BadZipFile
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn("Hit BadZipFile, returning []. Error", mock_logger.call_args[0][0])

    @patch("logging.Logger.error")
    def test_monitor_siem_logs_raises_json_error(self, mock_logger, _mock_data):
        test_state = {"next_token": "request.json error"}  # this forces our mocked response to raise JSON encode error
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching JSONDecodeError
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn("JSON", mock_logger.call_args[0][0])

    @patch("logging.Logger.debug")
    @patch("komand_mimecast.util.api.MimecastAPI.get_siem_logs", side_effect=Exception("negative seek"))
    def test_monitor_siem_logs_raises_negative_seek(self, mock_siem_logs, mock_logger, _mock_data):
        test_state = {"next_token": "negative_seek error"}  # this forces our mocked response to raise negative seek
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 500)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching negative seek
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn("negative seek", mock_logger.call_args[0][0])


class TestEventLogs(TestCase):
    def setUp(self) -> None:
        self.datetime_str = "2023-05-01T12:00:00-0400"
        self.output_data = {
            "acc": "ABC123",
            "Sender": "user@example.com",
            "datetime": self.datetime_str,
            "Rcpt": "user1@example.com",
            "aCode": "abcd123_abcd1234",
            "Dir": "Internal",
            "RcptHdrType": "To",
        }

        self.output_without_datetime = {
            "acc": "ABC123",
            "Sender": "user@example.com",
            "datetime": "",
            "Rcpt": "user1@example.com",
            "aCode": "abcd123_abcd1234",
            "Dir": "Internal",
            "RcptHdrType": "To",
        }

    def test_event_logs_get_dict(self):
        event = EventLogs(data=self.output_data)

        self.assertEqual(event.get_dict(), self.output_data)

    def test_event_logs_compare_to_datetime_when_event_is_newer(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 4, 1))
        self.assertTrue(expected_result)

    def test_event_logs_compare_to_datetime_when_event_is_older(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 6, 1))
        self.assertFalse(expected_result)
