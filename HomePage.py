from flask import Flask, request

app = Flask(__name__)

@app.route('/homepage')
def displayhomepage():
    return '''
    <!DOCTYPE html>
    <html>
    <title>EDA</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
    <style>
    body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
    </style>
    <head>
    <script>
    function startTime() {
      var today = new Date();
      var h = today.getHours();
      var m = today.getMinutes();
      var s = today.getSeconds();
      m = checkTime(m);
      s = checkTime(s);
      document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s;
      var t = setTimeout(startTime, 500);
    }
    function checkTime(i) {
      if (i < 10) {i = "0" + i};
      return i;
    }
    </script>
    </head>

    <body class="w3-light-grey" onload="startTime()">


    <div class="w3-content" style="max-width:1400px">


    <header class="w3-container w3-center w3-padding-32">
      <h1><b>EXPLORATORY DATA ANALYSIS</b></h1>
      <p>Welcome to the Exploratory Data Analysis of <span class="w3-tag">Google PlayStore Dataset</span></p>
    </header>


    <div class="w3-row">

      <div class="w3-col l8 s12">
      <pre>            <img id="myButton" src='/static/im1.png'/><script type="text/javascript">
                var images = ['/static/im1.png','/static/im2.png','/static/im3.png','/static/im4.png','/static/im5.png','/static/im6.png','/static/im7.png'],
                    i = 1;

                // preload
                for (var j=images.length; j--;) {
                    var img = new Image();
                    img.src = images[j];
                }

                // event handler
                document.getElementById('myButton').addEventListener('click', function() {
                    this.src = images[i >= images.length - 1 ? i = 0 : ++i];
                }, false);
            </script></pre>


      </div>



    <div class="w3-col l4">

      <div class="w3-card w3-margin w3-margin-top">

        <div class="w3-container w3-white">
          <h4><pre>  <b>Description About Our Project</b></pre></h4>
          <p>This Project implements the Exploratory Data Analysis of the google playstore along with Visualisation using Python and MongoDB. Furthermore, A Random Forest Regression Model and a Linear Regression Model have been used to Predict the ratings. </p>
        </div>
      </div><hr>

      <div class="w3-card w3-margin">
        <div class="w3-container w3-padding">
          <h4>CRUD Operations</h4>
        </div>
    	<ul class="w3-ul w3-hoverable w3-white">
          <li class="w3-padding-16" onclick="window.location.href='http://127.0.0.1:10000/search'">
            <span class="w3-large">Search</span><br>
          </li>
          <li class="w3-padding-16" onclick="window.location.href='http://127.0.0.1:13000/insert'">
            <span class="w3-large">Insert</span><br>
          </li>
          <li class="w3-padding-16" onclick="window.location.href='http://127.0.0.1:11000/update'">
            <span class="w3-large">Update</span><br>
          </li>
          <li class="w3-padding-16" onclick="window.location.href='http://127.0.0.1:12000/delete'">
            <span class="w3-large">Delete</span><br>
          </li>
    	</ul>
      </div>
      <div class="w3-card w3-margin">
        <div class="w3-container w3-padding">
          <h4>Prediction using Regression</h4>
        </div>
    	<ul class="w3-ul w3-hoverable w3-white">
          <li class="w3-padding-16" onclick="window.location.href='http://127.0.0.1:14000/regressor'">
            <span class="w3-large">Predict Ratings</span><br>
          </li>
    	</ul>
      </div>
      <div class="w3-card w3-margin">
        <div class="w3-container w3-padding">
          <h4>Description of Components of Project</h4>
        </div>
        <ul class="w3-ul w3-hoverable w3-white">
          <li class="w3-padding-16" onclick="window.location.href='https://gdcoder.com/random-forest-regressor-explained-in-depth/'">
            <span class="w3-large">Random Forest Regression Model</span><br>
          </li>
          <li class="w3-padding-16" onclick="window.location.href='https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86'">
            <span class="w3-large">Linear Regression Model</span><br>
          </li>

          </li>
        </ul>
      </div>
      <hr>


      <div class="w3-card w3-margin">
        <div class="w3-container w3-padding">
          <h4>DATABASE : MongoDB</h4>
        </div>
    	<ul class="w3-ul w3-hoverable w3-white">
          <li class="w3-padding-16" onclick="window.location.href='https://www.mongodb.com/'">
            <img src="/static/mongo.png" alt="Image" class="w3-left w3-margin-right" style="width:30px" >
            <span class="w3-large">About MongoDB</span><br>
          </li>
    	</ul>
      </div>
      

    </div>



    </div><br>


    </div>
    '''

if __name__ == '__main__':
    app.run(debug=True,port=9000)
