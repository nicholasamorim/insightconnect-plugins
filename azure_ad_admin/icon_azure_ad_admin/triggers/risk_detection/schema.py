# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides list of both user and sign-in linked risk detections and associated information about the detection"


class Input:
    
    FREQUENCY = "frequency"
    RISK_LEVEL = "risk_level"
    

class Output:
    
    RISK = "risk"
    

class RiskDetectionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "Poll frequency in seconds",
      "default": 60,
      "order": 1
    },
    "risk_level": {
      "type": "string",
      "title": "Risk Level",
      "description": "Risk level",
      "enum": [
        "low",
        "medium",
        "high",
        "hidden",
        "none",
        "all"
      ],
      "order": 2
    }
  },
  "required": [
    "risk_level"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RiskDetectionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk": {
      "$ref": "#/definitions/risk",
      "title": "Risk",
      "description": "Risk",
      "order": 1
    }
  },
  "required": [
    "risk"
  ],
  "definitions": {
    "geo_coordinates": {
      "type": "object",
      "title": "geo_coordinates",
      "properties": {
        "altitude": {
          "type": "string",
          "title": "Altitude",
          "description": "The altitude (height), in feet, above sea level",
          "order": 1
        },
        "latitude": {
          "type": "string",
          "title": "Latitude",
          "description": "The latitude, in decimal",
          "order": 2
        },
        "longitude": {
          "type": "string",
          "title": "Longitude",
          "description": "The longitude, in decimal",
          "order": 3
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "activity": {
          "type": "string",
          "title": "Activity",
          "description": "Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue",
          "order": 10
        },
        "activity_date_time": {
          "type": "string",
          "title": "Activity Date Time",
          "description": "Date and time that the risky activity occurred",
          "order": 14
        },
        "additional_info": {
          "type": "string",
          "title": "Additional Information",
          "description": "Additional information associated with the risk detection",
          "order": 20
        },
        "correlation_id": {
          "type": "string",
          "title": "Correlation ID",
          "description": "Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in",
          "order": 3
        },
        "detected_date_time": {
          "type": "string",
          "title": "Detected Date Time",
          "description": "Date and time that the risk was detected",
          "order": 15
        },
        "detection_timing_type": {
          "type": "string",
          "title": "Detection Timimg Type",
          "description": "Timing of the detected risk (real-time/offline). The possible values are notDefined, realtime, nearRealtime, offline, unknownFutureValue",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique ID of the risk detection",
          "order": 1
        },
        "ip_address": {
          "type": "string",
          "title": "IP Address",
          "description": "IP address of the client from where the risk occurred",
          "order": 12
        },
        "last_updated_date_time": {
          "type": "string",
          "title": "Last Updated Date Time",
          "description": "Date and time that the risk detection was last updated",
          "order": 16
        },
        "location": {
          "$ref": "#/definitions/sign_in_location",
          "title": "Location",
          "description": "Location of the client from where the risk occurred",
          "order": 13
        },
        "request_id": {
          "type": "string",
          "title": "Request ID",
          "description": "Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in",
          "order": 2
        },
        "risk_detail": {
          "type": "string",
          "title": "Risk Detail",
          "description": "Details of the detected risk. Details for this property are only available for Azure AD Premium P2 customers. P1 customers will be returned hidden",
          "order": 7
        },
        "risk_level": {
          "type": "string",
          "title": "Risk Level",
          "description": "Level of the detected risk",
          "order": 6
        },
        "risk_state": {
          "type": "string",
          "title": "Risk State",
          "description": "The state of a detected risky user or sign-in",
          "order": 5
        },
        "risk_type": {
          "type": "string",
          "title": "Risk Type",
          "description": "The type of risk event detected",
          "order": 4
        },
        "source": {
          "type": "string",
          "title": "Risk Level",
          "description": "Source of the risk detection. For example, activeDirectory",
          "order": 8
        },
        "token_issuer_type": {
          "type": "string",
          "title": "Token Issuer Type",
          "description": "Indicates the type of token issuer for the detected sign-in risk. The possible values are AzureAD, ADFederationServices, and unknownFutureValue",
          "order": 11
        },
        "user_display_name": {
          "type": "string",
          "title": "User Display Name",
          "description": "User display name",
          "order": 18
        },
        "user_id": {
          "type": "string",
          "title": "User ID",
          "description": "User ID",
          "order": 17
        },
        "user_principal_name": {
          "type": "string",
          "title": "User Principal Name",
          "description": "The user principal name (UPN) of the user",
          "order": 19
        }
      },
      "required": [
        "id"
      ],
      "definitions": {
        "geo_coordinates": {
          "type": "object",
          "title": "geo_coordinates",
          "properties": {
            "altitude": {
              "type": "string",
              "title": "Altitude",
              "description": "The altitude (height), in feet, above sea level",
              "order": 1
            },
            "latitude": {
              "type": "string",
              "title": "Latitude",
              "description": "The latitude, in decimal",
              "order": 2
            },
            "longitude": {
              "type": "string",
              "title": "Longitude",
              "description": "The longitude, in decimal",
              "order": 3
            }
          }
        },
        "sign_in_location": {
          "type": "object",
          "title": "sign_in_location",
          "properties": {
            "city": {
              "type": "string",
              "title": "City",
              "description": "City where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
              "order": 1
            },
            "country_or_region": {
              "type": "string",
              "title": "Country Or Region",
              "description": "Country code info (2 letter code) where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
              "order": 2
            },
            "geo_coordinates": {
              "$ref": "#/definitions/geo_coordinates",
              "title": "Geo Coordinates",
              "description": "Geo coordinates",
              "order": 3
            },
            "state": {
              "type": "string",
              "title": "State",
              "description": "State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
              "order": 4
            }
          },
          "definitions": {
            "geo_coordinates": {
              "type": "object",
              "title": "geo_coordinates",
              "properties": {
                "altitude": {
                  "type": "string",
                  "title": "Altitude",
                  "description": "The altitude (height), in feet, above sea level",
                  "order": 1
                },
                "latitude": {
                  "type": "string",
                  "title": "Latitude",
                  "description": "The latitude, in decimal",
                  "order": 2
                },
                "longitude": {
                  "type": "string",
                  "title": "Longitude",
                  "description": "The longitude, in decimal",
                  "order": 3
                }
              }
            }
          }
        }
      }
    },
    "sign_in_location": {
      "type": "object",
      "title": "sign_in_location",
      "properties": {
        "city": {
          "type": "string",
          "title": "City",
          "description": "City where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
          "order": 1
        },
        "country_or_region": {
          "type": "string",
          "title": "Country Or Region",
          "description": "Country code info (2 letter code) where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
          "order": 2
        },
        "geo_coordinates": {
          "$ref": "#/definitions/geo_coordinates",
          "title": "Geo Coordinates",
          "description": "Geo coordinates",
          "order": 3
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity",
          "order": 4
        }
      },
      "definitions": {
        "geo_coordinates": {
          "type": "object",
          "title": "geo_coordinates",
          "properties": {
            "altitude": {
              "type": "string",
              "title": "Altitude",
              "description": "The altitude (height), in feet, above sea level",
              "order": 1
            },
            "latitude": {
              "type": "string",
              "title": "Latitude",
              "description": "The latitude, in decimal",
              "order": 2
            },
            "longitude": {
              "type": "string",
              "title": "Longitude",
              "description": "The longitude, in decimal",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
