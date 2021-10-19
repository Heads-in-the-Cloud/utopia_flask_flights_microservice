from flask import Flask, request
app = Flask(__name__)

@app.route('/airports', methods = ['POST', 'GET'])
def getAirports():
    if request.method == 'GET':
        return "<h1>Return a JSONified object of all airports from db coming from mysql docker container</h1>"
    if request.method == 'POST':
        return "<h1>Take an object of a airport. Add it to shared db instance.</h1>"