# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    HOST = "host"
    KEY = "key"
    PASSWORD = "password"
    PORT = "port"
    USE_KEY = "use_key"
    USERNAME = "username"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "description": "Remote host to connect to. Can be over-ridden in actions",
      "order": 4
    },
    "key": {
      "$ref": "#/definitions/credential_secret_key",
      "description": "A base64 encoded SSH private key to use to authenticate to remote server. A newline is required after the beginning and before the end marker",
      "order": 3
    },
    "password": {
      "$ref": "#/definitions/credential_secret_key",
      "description": "Password authentication or password to decrypt provided private key. Either this or SSH private key is required",
      "order": 2
    },
    "port": {
      "type": "integer",
      "description": "Remote port to use",
      "default": 22,
      "order": 5
    },
    "use_key": {
      "type": "boolean",
      "title": "Use Keys",
      "description": "True to connect via key, false to connect via password",
      "order": 6
    },
    "username": {
      "type": "string",
      "description": "User to run command as",
      "order": 1
    }
  },
  "required": [
    "host",
    "port",
    "use_key",
    "username"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
