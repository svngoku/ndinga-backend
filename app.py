from flask import Flask, jsonify, request, redirect, url_for, make_response, render_template
from flask_restful import Resource, Api,reqparse
import json
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from pymongo import MongoClient
from tools.json_tools import JSONEncoder
from bson import ObjectId
import requests

from models.ki_fr import KgFr

app = Flask(__name__)

cors = CORS(app,allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],resources={r"/api/*": {"origins": "*"}})
client = MongoClient("mongodb://localhost:27017/")
ndinga_database = client["ndinga_nosql"]
kg_fr_collection = ndinga_database["ki_fr"]

api_uri = "/api/v1/kg_fr"

@app.route('/')
def index():
    return render_template('base.html', title='Home')

@app.route('/success/<traduction>')
def success(traduction):
   return 'Traduction du mot ' % traduction


@app.route('/dashbaord')
def dashboard():
    return render_template('home.html', title='Dashboard')


@app.route(api_uri+'/all', methods=['GET'])
def getAll():
    output = []
    for translation in kg_fr_collection.find():
        output.append({'kg': translation['ki'], 'fr': translation['fr']})
    return jsonify({"datas": output})

@app.route('/add', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template("kg_fr.form.html")

    if request.method == "POST":
        kg = request.form['kg']
        fr = request.form['fr']
        translate_word_id = kg_fr_collection.insert({'ki': kg, 'fr': fr})
        new_translation = kg_fr_collection.find_one({'_id': translate_word_id })
        output = {'ki' : new_translation['ki'], 'fr' : new_translation['fr']}
        print(jsonify(output))
        return redirect(url_for("dashboard"))



@app.route('/test')
def test():
    req = requests.get("http://localhost:5000/api/v1/kg_fr/all")
    return render_template('test.html', title="Test", kg_fr_data = req)
@app.route('/base')
def base():
    return render_template('base.html', title='Base')

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)

