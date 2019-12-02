import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from pymongo import MongoClient
from sklearn.linear_model import LinearRegression
from flask import Flask, request



app = Flask(__name__)

@app.route('/regressor', methods = ['POST','GET'])
def regressor():
    if request.method == 'POST':
        mongo_client=MongoClient()
        db=mongo_client.testdb
        completeData=pd.DataFrame(list(db.testcollection.find({})))
        completeData=completeData.drop(["_id","App","Category","Type","Content Rating","Genres","Last Updated","Current Ver","Android Ver"],axis=1)



        completeData = completeData.dropna()
        completeData = completeData.reset_index(drop=True)
        #print(completeData)

        index_for_deletion = []
        for i in completeData.index:
            if "NaN" in completeData['Rating'][i]:
                index_for_deletion.append(i)
                continue
            if completeData['Size'][i] == 'Varies with device':
                index_for_deletion.append(i)
                continue
            if 'Free' in completeData['Installs'][i]:
                index_for_deletion.append(i)
                continue
            completeData['Reviews'][i]=int(completeData['Reviews'][i])
            if '+' in completeData['Size'][i]:
                completeData['Size'][i] = completeData['Size'][i][:-1]
            if ',' in completeData['Size'][i]:
                completeData['Size'][i] = completeData['Size'][i].replace(',','')
            if 'M' in completeData['Size'][i]:
                completeData['Size'][i] = float(completeData['Size'][i][:-1])
            elif 'k' in completeData['Size'][i]:
                completeData['Size'][i] = completeData['Size'][i][:-1]
                completeData['Size'][i] = float(completeData['Size'][i])*0.001
            else:
                completeData['Size'][i] = float(completeData['Size'][i])
            if '+' in completeData['Installs'][i]:
                completeData['Installs'][i] = completeData['Installs'][i][:-1]
                completeData['Installs'][i] = int(completeData['Installs'][i].replace(',',''))
            else:
                completeData['Installs'][i] = float(completeData['Installs'][i].replace(',',''))
            if '$' in completeData['Price'][i]:
                completeData['Price'][i] = float(completeData['Price'][i][1:])
            else:
                completeData['Price'][i] = float(completeData['Price'][i])

        for x in index_for_deletion:
            completeData = completeData.drop(x)
        completeData = completeData.reset_index(drop=True)



        X = completeData.iloc[:,1:].values
        y = completeData.iloc[:,0].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)



        regressor = RandomForestRegressor(n_estimators=250, random_state=0)
        regressor.fit(X_train, y_train)
        y_pred_rfr = regressor.predict(X_test)


        linearRegressor = LinearRegression()
        linearRegressor.fit(X_train, y_train)
        y_pred_lr = linearRegressor.predict(X_test)

        pred = pd.DataFrame()
        pred["Actual Ratings"] = pd.Series(y_test)
        pred["RFR Ratings"] = pd.Series(y_pred_rfr)
        pred["LR Ratings"] = pd.Series(y_pred_lr)
        reviews = request.form.get('reviews')
        size = request.form.get('size')
        installs = request.form.get('installs')
        price = request.form.get('price')
        pred_with = [[reviews,size,installs,price]]
        pred_with = sc.transform(pred_with)
        pred_value_rfr = regressor.predict(pred_with)
        pred_value_lr = linearRegressor.predict(pred_with)
        return '''<p>Random Forest Regressor Rating Prediction {}</p>
        <p>Linear Regression Model Rating Prediction {}</p>
        Comparison of Two Regressions using Test cases\n
        <pre align="center">{}</pre>'''.format(pred_value_rfr[0],pred_value_lr[0],pred.to_html())

    elif request.method == 'GET':
        return '''
        <!DOCTYPE html>
        <html>
        <title>Regression Models</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <style>
        body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
        .hmpg {
        position: absolute;
        left: 1220px;
        top: 600px;
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
          <h1><b>Prediction Models: Random Forest Regression and Linear Regression</b></h1>
          <p>Welcome to the Prediction Page of <span class="w3-tag">Google PlayStore Dataset</span></p>
        </header>

        <form method="POST">
        <pre align="center">Reviews         <input type="text" name="reviews">
        <pre align="center">Size            <input type="text" name="size">
        <pre align="center">Installs        <input type="text" name="installs">
        <pre align="center">Price           <input type="text" name="price">
        <pre align="center">     <input type="submit" class="button" value="Predict">
        <pre class="hmpg"><input type="button" class="button" onclick="location.href='http://127.0.0.1:9000/homepage';" value="Home Page" /></pre>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True,port=14000)

"""
pred_with = [['250','100000','10.0','0.0']]
pred_with = sc.transform(pred_with)
pred_value = regressor.predict(pred_with)
print("Predicted Rating: ",pred_value[0])
"""
