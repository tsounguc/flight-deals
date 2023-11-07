import os

from flight_data import FlightData
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight: FlightData):
        self.price = flight.price
        self.departure_city = flight.departure_city
        self.departure_airport_code = flight.departure_airport_code
        self.arrival_city = flight.arrival_city
        self.arrival_airport_code = flight.arrival_airport_code
        self.date_from = flight.date_from
        self.date_to = flight.date_to


        self.message = (f'Low price alert! Only ${self.price} to fly from '
                        f'\n{self.departure_city}-{self.departure_airport_code} to {self.arrival_city}-{self.arrival_airport_code}, from'
                        f'\n{self.date_from.split("T")[0]} to {self.date_to.split("T")[0]}')

    def send_notification(self):
        print(self.message)
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

    def send_email(self, to_email):
        my_email = "tsounguc@mail.gvsu.edu"
        password = os.environ.get("password")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Secure connection with Transport Layer Security
            connection.starttls()
            # Login to account
            connection.login(user=my_email, password=password)
            # Send email
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Low price alert! \n\n{self.message}")



