from data_manager import DataManager
from flight_search import FlightSearch
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
# import requests
#
# endpoint = "https://api.tequila.kiwi.com/locations/query"
# api_key = "OcLwyb8_8MOjZL6uaduhOUynugrYgZ8q"
# headers = {
#     "apikey": api_key
# }
# parameters = {
#     "term": "Paris",
#     "location_types": "city"
# }
#
# response = DataManager()
# response.raise_for_status()
# data = response.json()
# print(data["locations"][0]['code'])
#
# sheety_response = requests.get(url="https://api.sheety.co/0d6888b4ea372773b01f568e0d405d57/flightDeals/prices")
# print(sheety_response.json()["prices"])

data_manager = DataManager()
flight_search = FlightSearch()

flights_data = data_manager.get_flights()

for row in flights_data:
    city = row['city']
    row_id = row['id']
    print(city)
    city_code = flight_search.get_city_code(city)
    data_manager.set_flight_code(city_code, row_id)




