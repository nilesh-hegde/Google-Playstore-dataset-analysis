from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request
import json

mongo_client=MongoClient()
db=mongo_client.testdb

app = Flask(__name__)

@app.route('/insert', methods=['POST','GET'])
def inserting():
    if request.method == 'POST':
        app = request.form.get('app')
        category = request.form.get('category')
        rating = request.form.get('rating')
        reviews = request.form.get('reviews')
        size = request.form.get('size')
        installs = request.form.get('installs')
        type = request.form.get('type')
        price = request.form.get('price')
        cr = request.form.get('cr')
        genres = request.form.get('genres')
        data = {"App":app,"Category":category,"Rating":rating,"Reviews":reviews,"Size":size,"Installs":installs,"Type":type,"Price":price,"Content Rating":cr,"Genres":genres}
        dt = db.cleandata.insert_one(data)
        return 'Record has been inserted'

    elif request.method == 'GET':
        return '''
        <!DOCTYPE html>
        <html>
        <title>Insert MongoDB</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <style>
        body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
        .hmpg {
        position: absolute;
        left: 1220px;
        top: 880px;
        }
        .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 5px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 2px 2px;
        border-radius: 12px;
        }
        </style>
        <head>
        </head>
        <body class="w3-light-grey" onload="startTime()">


        <div class="w3-content" style="max-width:1400px">


        <header class="w3-container w3-center w3-padding-32">
          <h1><b>CRUD Operations : INSERTION</b></h1>
          <p>Welcome to the Query Page of <span class="w3-tag">Google PlayStore Dataset</span></p>
        </header>

        <form method="POST">
        <pre align="center">App             <input type="text" name="app">
        <pre align="center">Category        <input type="text" name="category">
        <pre align="center">Rating          <input type="text" name="rating">
        <pre align="center">Reviews         <input type="text" name="reviews">
        <pre align="center">Size            <input type="text" name="size">
        <pre align="center">Installs        <input type="text" name="installs">
        <pre align="center">Type            <input type="text" name="type">
        <pre align="center">Price           <input type="text" name="price">
        <pre align="center">Content Rating  <input type="text" name="cr">
        <pre align="center">Genres          <input type="text" name="genres">
        <pre align="center">     <input type="submit" class="button" value="Insert">
        <pre class="hmpg"><input type="button" class="button" onclick="location.href='http://127.0.0.1:9000/homepage';" value="Home Page" /></pre>
        </form>'''

if __name__ == '__main__':
    app.run(debug=True,port=13000)
