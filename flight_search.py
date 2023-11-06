import os

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.api_key = os.environ.get("flight_api_key")

    def get_city_code(self, city):
        headers = {
                "apikey": self.api_key
            }
        parameters = {
            "term": city,
            "location_type": "city"
        }
        response = requests.get(url=self.endpoint, params=parameters, headers=headers)
        response.raise_for_status()
        code = response.json()["locations"][0]['code']
        print(code)
        return code
