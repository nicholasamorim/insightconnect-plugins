# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Change a user password by an administrator with appropriate permissions"


class Input:
    NEW_PASSWORD = "new_password"
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    

class ChangeUserPasswordInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "new_password": {
      "type": "string",
      "title": "New Password",
      "displayType": "password",
      "description": "The new password",
      "format": "password",
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID to password change",
      "order": 1
    }
  },
  "required": [
    "new_password",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ChangeUserPasswordOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
