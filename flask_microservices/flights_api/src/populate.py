from faker      import Faker
from random     import randrange
from datetime   import timedelta
from datetime   import datetime
from .models import *                                                                                              
from .models import db

import requests
import json

fake = Faker()

PORT = 5000

apiRoute = f'http://localhost:{PORT}/flights'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

departureDate1 = datetime.strptime('11/3/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
departureDate2 = datetime.strptime('11/30/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def populateFlights():
    for i in range(100):
        flight = []
        flight.append({
            "route_id": fake.pyint(min_value=1, max_value=14, step=1),
            "airplane_id": fake.pyint(min_value=1, max_value=4, step=1),
            "departure_time": "2021-09-25 21:49:00",
            # "departure_time": random_date(departureDate1, departureDate2),
            "reserved_seats": fake.pyint(min_value=1, max_value=300, step=1),
            "seat_price": fake.pyfloat(left_digits=3, right_digits=2, min_value=0, max_value=300)
        })
        for i in range(len(flight)):
            r = requests.post(apiRoute, data=json.dumps(flight[i]), headers=headers)
            print(r.status_code)

populateFlights()

    



