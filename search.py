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

@app.route('/search', methods = ['POST','GET'])
def searching():
    if request.method == 'POST':
        data = request.form.get('data')
        query = json.loads(data)
        df = pd.DataFrame(db.cleandata.find(query))
        return '''<p align="center">{}<p>'''.format(df.to_html())
    elif request.method == 'GET':
        return '''
        <!DOCTYPE html>
        <html>
        <title>Search MongoDB</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <style>
        body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
        .hmpg {
        position: absolute;
        left: 1220px;
        top: 580px;
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
          <h1><b>CRUD Operations : SEARCHING</b></h1>
          <p>Welcome to the Query Page of <span class="w3-tag">Google PlayStore Dataset</span></p>
        </header>
        <form method="POST">
        <pre align = "center">
        Query <input type="text" name="data"></pre>
        <pre align = "center"><input type="submit" class = "button" value="Search"></pre>
        <pre class="hmpg"><input type="button" class="button" onclick="location.href='http://127.0.0.1:9000/homepage';" value="Home Page" /></pre>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True,port=10000)
