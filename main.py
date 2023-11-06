from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()

sheety_data = data_manager.get_data()

for row in sheety_data:
    flight = FlightData()
    city = row['city']
    row_id = row['id']
    if row['iataCode'] == '':
        city_code = flight_search.get_city_code(city)
        data_manager.set_iata_code(city_code, row_id)

sheety_data = data_manager.get_data()
for row in sheety_data:
    flight_search.get_flights(price=row['lowestPrice'], city_code=row['iataCode'])


