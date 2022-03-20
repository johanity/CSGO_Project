from flask import Flask, render_template, jsonify, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db

players = db.csgo.find()

@app.route("/add_one")
def add_one():
    name = input("Input name: ")
    team = input("Input team: ")
    db.csgo.insert_one({'name': name, 'team': team})
    return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template('index.html', players = players)

@app.route("/add_many")
def add_many():
    db.todos.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return Flask.jsonify(message="success")