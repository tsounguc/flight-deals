import os
from datetime import datetime, timedelta
import requests

from flight_data import FlightData


# from twilio.rest import Client


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        self.api_key = os.environ.get("flight_api_key")
        self.headers = {
            "apikey": self.api_key
        }

    def get_city_code(self, city):
        parameters = {
            "term": city,
            "location_type": "city"
        }
        response = requests.get(url=f"{self.url}/locations/query", params=parameters, headers=self.headers)
        response.raise_for_status()
        code = response.json()["locations"][0]['code']
        return code

    def get_flights_data(self, price, city_code):
        today = datetime.now()
        tomorrow = today + timedelta(1)
        six_months_later = tomorrow + timedelta(weeks=24.0)
        parameters = {
            "fly_from": "DEN",
            "fly_to": city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_later.strftime("%d/%m/%Y"),
            "price_to": price,
            "max_stop_over": 0,
            "curr": "USD",
            "one_for_city": 1
        }
        response = requests.get(url=f"{self.url}/v2/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        flights_data = response.json()["data"]
        flights_list = [FlightData(price=flight_data["price"],
                                   departure_city=flight_data["cityFrom"],
                                   departure_airport_code=flight_data["flyFrom"],
                                   arrival_city=flight_data["cityTo"],
                                   arrival_airport_code=flight_data["flyTo"],
                                   date_from=flight_data["local_departure"],
                                   date_to=flight_data["local_arrival"],
                                   ) for flight_data in flights_data
                        if price > flight_data["price"]]
        return flights_list
