import flask
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb+srv://johanity:kevinvle@cluster0.mzkq5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/add_one")
def add_one():
    title = input("Intput title: ")
    body = input("Input body: ")
    db_object = {'title': title, 'body': body}
    db.csgo.insert_one({'_id': 1, 'title': title, 'body': body})
    return flask.jsonify(message=db_object)

@app.route("/")
def home():
    csgo = db.csgo.find()
    return flask.jsonify([todo for todo in csgo])

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
    return flask.jsonify(message="success")