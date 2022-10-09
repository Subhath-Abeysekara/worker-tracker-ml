# This is a sample Python script
import json

import numpy as np
import model as m
#import Ml model
import model2 as m2

#import flask library for build apis
from flask import Flask,request, jsonify
#flask cors handing
from flask_cors import CORS , cross_origin



import pickle

app = Flask(__name__)
#enable cross origin for any ip
CORS(app , resources={r"/":{"origins":"*"}})

#Home Api
@app.route("/")
def main():
    return "hello world"

#First Page
@app.route("/home")
@cross_origin()
def home():
    return "First Page"

#Api for get suitable projects
@app.route("/model" , methods = ["GET"])
@cross_origin()
def model():
    #get rating value as api parameter
    id = request.args.get('id')
    print('id '+id)

    #Get suitable five projects
    first_five_projects = m2.func1(int(id))
    print(first_five_projects)
    #Listed projectIds to send response
    first_five_projects_list = first_five_projects['PrjecttId'].tolist()
    #send response to api request
    return first_five_projects_list

if __name__ == '__main__':
    app.debug = True
    #init api port and ip address of the server
    app.run(host='0.0.0.0',port=5000)