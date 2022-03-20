from flask import Flask, render_template, jsonify, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/add_one")
def add_one():
    name = input("Input name: ")
    if db.csgo.find_one({'name': name}):
        print("already")
    else:
        team = input("Input team: ")
        url = input("Url: ")
        db.csgo.insert_one({'name': name, 'team': team, 'url': url})
        
    return redirect(url_for("home"))

@app.route("/")
def home():
    players = db.csgo.find()
    return render_template('index.html', players = players)

@app.route("/add_many")
def add_many():
    many = []
    numAdditions = int(input('How many player/team submissions would you like to make?: '))
    for submission in range(numAdditions):
        name = input("Intput name: ")
        if db.csgo.find({'name': name}):
            print("already")
        else:
            team = input("Input team: ")
            many.append({'name': name, 'team': team})
    if many:
        db.csgo.insert_many(submission for submission in many)
    return redirect(url_for("home"))




if __name__ == '__main__':
    app.debug = True
    app.run()