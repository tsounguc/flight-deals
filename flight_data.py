class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city, arrival_city, arrival_airport_code,
                 date_from, date_to):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.arrival_airport_code = arrival_airport_code
        self.arrival_city = arrival_city
        self.date_from = date_from
        self.date_to = date_to
