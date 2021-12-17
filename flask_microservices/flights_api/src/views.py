# Flask/Python Packages
from flask import request, jsonify, make_response
from . import app
from .models.flight import *                                                                 
import json
from .database import *
    
@app.route('/airports', methods = ['POST', 'GET'])
def getPostAirport():
    if request.method == 'GET':
        airports = Airport.query.all()
        all_airports = []
        for airport in airports:                                                 
            new_airports = {
                 "iata_id": airport.iata_id,
                 "city": airport.city
             }
            all_airports.append(new_airports)
        return json.dumps(all_airports), 200
    if request.method == 'POST':
        data = request.get_json()
        iata_id = data['iata_id']
        city = data['city']
        airport = Airport(iata_id=iata_id, city=city)
        db.session.add(airport)
        db.session.commit()
        return json.dumps("Added Airport"), 200

@app.route('/airports/<iata_id>', methods = ['DELETE', 'PATCH'])
def deletePatchAirport(iata_id):
    if request.method == 'DELETE':
        Airport.query.filter_by(iata_id=iata_id).delete()
        db.session.commit()
        return json.dumps("Deleted Airport"), 200
    if request.method == "PATCH":
        data = request.get_json()
        new_iata_id = data['iata_id']
        airport_to_update = Airport.query.filter_by(iata_id=iata_id).all()[0]
        airport_to_update.iata_id = new_iata_id
        db.session.commit()
        return json.dumps("Edited Airport Success"), 200

@app.route('/routes', methods = ['GET', 'POST'])
def getPostRoutes():
    if request.method == 'GET':
        routes = Route.query.all()
        all_routes = []
        for route in routes:
            new_routes = {
                "id": route.id,
                "origin_id": route.origin_id,
                "destination_id": route.destination_id
            }
            all_routes.append(new_routes)
        return json.dumps(all_routes), 200
    if request.method == 'POST':
        data = request.get_json()
        origin_id = data['origin_id']
        destination_id = data['destination_id']
        route = Route(origin_id=origin_id, destination_id=destination_id)
        db.session.add(route)
        db.session.commit()
        return json.dumps("Added New Route"), 200

@app.route('/routes/<route_id>', methods = ['DELETE', 'PATCH'])
def deletePatchRoute(route_id):
    if request.method == 'DELETE':
        Route.query.filter_by(id=route_id).delete()
        db.session.commit()
        return json.dumps("Deleted Route"), 200
    if request.method == "PATCH":
        data = request.get_json()
        new_route_id = data['route_id']
        route_to_update = Route.query.filter_by(id=route_id).all()[0]
        route_to_update.route_id = route_to_update
        db.session.commit()
        return json.dumps("Edited Route Success"), 200

@app.route('/flights', methods = ['GET', 'POST'])
def getPostFlights(**kwargs):
    if request.method == 'GET':
        flights = Flight.query.all()
        all_flights = []
        for flight in flights:
            new_flights = {
                "id": flight.id,
                "Route": flight.route_id,
                "Airplane Type": flight.airplane_id,
                "Route": flight.route_id,
                "Airplane Type": flight.airplane_id
            }
            all_flights.append(new_flights)
        return json.dumps(all_flights), 200
    if request.method == 'POST':
        data = request.get_json()
        route_id = data['route_id']
        airplane_id = data['airplane_id']
        departure_time = data['departure_time']
        reserved_seats = data['reserved_seats']
        seat_price = data['seat_price']
        flight = Flight(
                    route_id=route_id, 
                    airplane_id=airplane_id, 
                    departure_time=departure_time,
                    reserved_seats=reserved_seats,
                    seat_price=seat_price
                    )
        db.session.add(flight)
        db.session.commit()
        return json.dumps("Added New Flight"), 200







