import datetime
from flask import Flask
from sqlalchemy import create_engine
from flask_flights_mc import db
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("")
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

class Airport(db.Model):
    iata_id = db.Column(db.String(3), primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Airport( '{self.iata_id}', '{self.city}', '{self.date_posted}') "