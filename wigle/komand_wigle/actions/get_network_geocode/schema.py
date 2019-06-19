# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESSCODE = "addresscode"
    

class Output:
    RESULTS = "results"
    

class GetNetworkGeocodeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "addresscode": {
      "type": "string",
      "title": "Address Code",
      "description": "An address string, Street, City, State/Region, Country",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetNetworkGeocodeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Matched geocode",
      "items": {
        "$ref": "#/definitions/geocode"
      },
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "geocode": {
      "type": "object",
      "title": "geocode",
      "properties": {
        "address": {
          "type": "object",
          "title": "Address",
          "order": 1
        },
        "boundingbox": {
          "type": "array",
          "title": "Bounding Box",
          "items": {
            "type": "number"
          },
          "order": 9
        },
        "display_name": {
          "type": "string",
          "title": "Display Name",
          "order": 8
        },
        "importance": {
          "type": "number",
          "title": "Importance",
          "order": 4
        },
        "lat": {
          "type": "number",
          "title": "Latitude",
          "order": 2
        },
        "license": {
          "type": "string",
          "title": "License",
          "order": 6
        },
        "lon": {
          "type": "number",
          "title": "Longitude",
          "order": 3
        },
        "osm_type": {
          "type": "string",
          "title": "OSM Type",
          "order": 7
        },
        "place_id": {
          "type": "integer",
          "title": "Place ID",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
