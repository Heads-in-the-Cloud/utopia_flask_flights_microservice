from faker      import Faker
from random     import randrange
from datetime   import timedelta
from datetime   import datetime
from .models import *                                                                                              
from .models import db

import requests
import json

fake = Faker()

PORT = 3001

apiRoute = f'http://localhost:{PORT}/bookings'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

departureDate1 = datetime.strptime('11/3/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
departureDate2 = datetime.strptime('11/30/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def populateBookings():
    for i in range(100):
        booking = []
        booking.append({
            "is_active": fake.pyint(min_value=1, max_value=3, step=1),
            
        })
        for i in range(len(booking)):
            r = requests.post(apiRoute, data=json.dumps(booking[i]), headers=headers)
            print(r.status_code)

populateBookings()

    



