import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.environ.get("SHEETY_ENDPOINT")

    def get_flights(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        flights_data = response.json()["prices"]
        print(flights_data)
        return flights_data

    def set_flight_code(self, code, object_id):
        body = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{object_id}", json=body)
        response.raise_for_status()
        print(response.text)
        print(response.json())

