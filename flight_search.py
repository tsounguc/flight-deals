import os
from datetime import datetime, timedelta
import requests
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

    def get_flights(self, price, city_code):
        today = datetime.now()
        tomorrow = today + timedelta(1)
        six_months_later = tomorrow + timedelta(weeks=24.0)
        parameters = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_later.strftime("%d/%m/%Y"),
            "price_to": price,
            "max_stop_over": 0,
            "curr": "GBP",
            "one_for_city": 1
        }
        response = requests.get(url=f"{self.url}/v2/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        data = response.json()["data"]
        price = 0
        for flight in data:
            if price < flight["price"]:
                price = flight["price"]
                body = f'Low price alert! Only ${flight["price"]} to fly from \n{flight["cityFrom"]}-{flight["flyFrom"]} to {flight["cityTo"]}-{flight["flyTo"]}, from \n{tomorrow.strftime("%Y-%m-%d")} to {six_months_later.strftime("%Y-%m-%d")}'
                print(body)
                # account_sid = os.environ['TWILIO_ACCOUNT_SID']
                # auth_token = os.environ['TWILIO_AUTH_TOKEN']
                # client = Client(account_sid, auth_token)
                #
                # message = client.messages \
                #     .create(
                #     from_='+15557771212',
                #     body=body,
                #     to='+15559991111'
                # )
                #
                # print(message.body)

