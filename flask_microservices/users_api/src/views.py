# Flask/Python Packages
from flask import request, jsonify, make_response
from . import app
from .models import *                                                                 
import json
from .database import *
    
    
@app.route('/register', methods = ['POST'])
def registerUser():
    return 200






