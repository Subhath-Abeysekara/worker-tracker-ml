# This is a sample Python script
import json
import numpy as np
import model as m

from flask import Flask,request, jsonify
import pickle

app = Flask(__name__)

names = ["subhath","diniki"]

model = pickle.load(open("model.pkl" , "rb"))

projectIds = model[['title']].values.tolist()

print(projectIds)

np_array = model.to_numpy()
l_list = model.values.tolist()

print(np_array)
print(l_list)


@app.route("/")
def main():
    return "hello world"

@app.route("/home")
def home():
    return names

@app.route("/model" , methods = ["GET"])
def model():
    id = request.args.get('id')
    print('id '+id)
    students = [
        {'name':"subhath" , 'age':24},
        {'name':"diniki" , 'age':23}
    ]

    student = {'name':"subhath" , 'age':24}

    first_five_projects = m.func(int(id))
    print(first_five_projects)
    first_five_projects_list = first_five_projects['title'].tolist()

    return first_five_projects_list

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)