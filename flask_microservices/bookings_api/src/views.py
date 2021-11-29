# Flask/Python Packages
from flask import request, jsonify, make_response
from . import app
from .models import *                                                                 
import json
from .database import *
    
@app.route('/booking', methods = ['POST', 'GET'])
def getBookings():
    if request.method == 'GET':
        bookings = Booking.query.all()
        all_bookings = []
        for booking in bookings:                                                 
            new_bookings = {
                 "iata_id": airport.iata_id,
                 "city": airport.city
             }
            all_bookings.append(new_bookings)
        return json.dumps(all_bookings), 200
    else:
        return 'Error'






