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
        name = input("Input name: ")
        team = input("Input team: ")
        many.append({'name': name, 'team': team})
    db.csgo.insert_many(submission for submission in many)
    return redirect(url_for("home"))

@app.route("/update")
def update(): 

    #verify if change operation is accurate
    verification = input('Are you sure you want to change a player card? (Yes/No)')

    #if operation is not accurate
    if verification == 'No':
        return redirect(url_for("home"))


    #if operation is accurate
    if verification == 'Yes':

        name = input("Enter player Name: ")
        

        print('''
        
        Please make a selection:

        (p) - Change a player name.
        (t) - Change a team name.
        (b) - Change both player and team name.

        ''')

        #Selection Input
        whatChange = input()
        filter = { "name" : name}
        if whatChange == 'p':
            new_name = input('Enter updated player name: ')
            db.csgo.update_one(filter, { "$set": { 'name': new_name } }, upsert = True )

        if whatChange == 't':
            new_team= input('Enter updated team name: ')
            db.csgo.update_one(filter, { "$set": { 'team': new_team } }, upsert = True )

        if whatChange == 'b':
            new_name = input('Enter updated player name: ')
            new_team= input('Enter updated team name: ')
            db.csgo.update_one(filter, { "$set": { 'team': new_team } }, upsert = True )
            db.csgo.update_one(filter, { "$set": { 'name': new_name } }, upsert = True )

    #success message and redirect to home
    print('Player Card Successfully Updated')
    return redirect(url_for("home"))

@app.route("/<string:team>")
def display_team(team):
    specificPlayers = [player["name"] for player in db.csgo.find({"team": team})]
    if specificPlayers:
        return jsonify(message = specificPlayers)
    else:
        return jsonify(message = "Not Found")

#@app.route("/update_many")
#def update_many():   




if __name__ == '__main__':
    app.debug = True
    app.run()