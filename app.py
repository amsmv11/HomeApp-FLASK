#!/usr/bin/env python
# encoding: utf-8

"""
APP RUNS ON PORT 5000
"""
import json
from flask import Flask, request, jsonify, redirect, render_template, url_for
import sqlite3
import hashlib

app = Flask(__name__)





@app.route("/get/", methods=['POST'])
def getParameters():
    dict_request = request.get_json(force=True)

    return dict_request


@app.route("/users/", methods=['POST'])
def createUser():
    dict_request = request.get_json(force=True)
    name = str(dict_request["username"])
    password = str(dict_request["password"])
    if name != "" and password != "":
        name = name.replace("<", "")
        name = name.replace(">", "")
        name = name.replace("script", "")
        name = name.replace("=", "")
        name = name.replace(";", "")
        name = name.replace(":", "")

        result = hashlib.md5(password.encode()) 
        res = result.hexdigest()

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", (name, res))
        conn.commit()
        conn.close()
        return redirect("/users/list")
    else:
        return "<h1>ERROR: username and password missing</h1>"


@app.route("/users/list/", methods=['GET'])
def listUsers():
    res = "<h1>List of all users</h1> <br> <ul>"

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    conn.commit()
    query = c.fetchall()
    conn.close()

    if query != []:
        for id, user, password in query:
            user = user.replace("<", "")
            user = user.replace(">", "")
            user = user.replace("script", "")
            user = user.replace("=", "")
            user = user.replace(";", "")
            user = user.replace(":", "")
            res += "<li> Username: " + user + " <br> Password: " + password + "</li>"

    else:
        res += "<li>EMPTY_LIST</li>"

    res += "</ul>"
    return res


@app.route("/redirect/", methods=['GET'])
def redirectTest():
    return redirect("https://www.google.com")

'''
@app.route("/<string:name>/", methods=['GET'])
def helloName(name):
    return "Hi " + name + "! \nDocker is easy"
'''
@app.route("/repeatName/<string:name>/<int:nr>/", methods=['GET', 'POST'])
def helloNameTimesNr(name, nr):
    response = ""
    if request.method == "POST":
        response += "POST METHOD\n"
    else:
        response += request.method + "\n"
    for i in range(nr):
        response += "Hello " + name +"!\n"
    return jsonify({'response':response})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/f1')
def f1():
    return render_template('f1.html')

@app.route('/saveLocation', methods=['GET', 'POST'])
def saveLocation():
    if request.method == "GET":
        return render_template('saveLocation.html')

    elif request.method == "POST":
        name = request.form['carro'].replace(";","")
        street = request.form['rua'].replace(";","")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("Delete FROM cars WHERE name = '{}'".format(name)  )
        conn.commit()

        c.execute("INSERT INTO cars (name, street) VALUES (?, ?)", (name, street))
        conn.commit()

        conn.close()
        return redirect(url_for("index"))


@app.route('/findDevice')
def findDevice():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM cars ")
    conn.commit()
    car_list = c.fetchall()
    conn.close

    return render_template('findDevice.html', list=car_list)

@app.route('/shoppingList', methods=['GET', 'POST', 'DELETE'])
def shoppingList():
    if request.method == "GET":
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM shopping ")
        conn.commit()
        shopping_list = c.fetchall()
        conn.close
        return render_template('shoppingList.html', list=shopping_list)

    elif request.method == "POST":
        name = request.form["item_to_add"].replace("script", "")
        name = name.replace(";" , "")
        name = name.replace("<" , "")
        name = name.replace(">" , "")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO shopping (name) VALUES (?)", (name,)  )
        conn.commit()
        return redirect(url_for("shoppingList"))

@app.route('/shoppingListRemove', methods=['POST'])
def shoppingListRemove():
    name = request.form["item_to_remove"].replace("script", "")
    name = name.replace(";" , "")
    name = name.replace("<" , "")
    name = name.replace(">" , "")
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM shopping WHERE name = '{}'".format(name)  )
    print("DELETE FROM shopping WHERE name = '{}'".format(name) )
    conn.commit()
    return redirect(url_for("shoppingList"))




'''
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('./data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('./data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('./data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('./data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
'''
# app.run(debug=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
