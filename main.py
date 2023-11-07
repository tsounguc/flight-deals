from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

# Get data from google sheet with data manager
sheety_data = data_manager.get_flight_data()

# Populate iata column with data from flight
for row in sheety_data:
    # Save city name in a variable
    city_name = row['city']
    row_id = row['id']

    if row['iataCode'] == '':
        city_code = flight_search.get_city_code(city_name)
        data_manager.set_iata_code(city_code, row_id)

sheety_data = data_manager.get_flight_data()
price = 0
notification_manager = None
for row in sheety_data:
    flights = flight_search.get_flights_data(price=row['lowestPrice'], city_code=row['iataCode'])
    for flight in flights:
        notification_manager = NotificationManager(flight)
        notification_manager.send_notification()

users_data = data_manager.get_users_data()
for row in users_data:
    if row["email"] != "":
        notification_manager.send_email(row['email'])
