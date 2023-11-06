import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.environ.get("SHEETY_ENDPOINT")

    def get_data(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        flights_data = response.json()["prices"]
        return flights_data

    def set_iata_code(self, code, object_id):
        body = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{object_id}", json=body)
        response.raise_for_status()

