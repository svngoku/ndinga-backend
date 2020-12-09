from flask import Flask, jsonify, request, make_response, render_template
from flask_restful import Resource, Api,reqparse
from flask_cors import CORS
import json
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from tools.json_tools import JSONEncoder
from bson import ObjectId

# from models.ki_fr import KgFr

app = Flask(__name__)

cors = CORS(app,allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],resources={r"/api/*": {"origins": "*"}})
client = MongoClient("mongodb://localhost:27017/")
ndinga_database = client["NDINGA"]
kg_fr_collection = ndinga_database["ki_fr"]

@app.route('/')
def index():
    return render_template('base.html', title='Home')

@app.route('/dashbaord')
def dashboard():
    return render_template('home.html', title='Dashboard')

@app.route('/api/v1/kg_fr/all', methods=['GET'])
def getAll():
    output = []
    for translation in kg_fr_collection.find():
        output.append({'kg': translation['ki'], 'fr': translation['fr']})
    return jsonify({"datas": output})

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)

