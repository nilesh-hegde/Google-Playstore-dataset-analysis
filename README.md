# Google-Playstore-dataset-analysis

1. This project involves the Exploratory Data Analysis(EDA) of Google Playstore Dataset.
2. The Dataset is available for free and can e downloaded from Kaggle website.
3. There is an in-depth EDA in the file 'eda.py'.
4. Important EDA is found in 'dataanalytics.py'.
5. Pymongo is used as the connector.
6. The Database used is MongoDB.
7. Flask has been Used for developing UI.
8. Random Forest Regressor and Linear Regression Model has been used to prdict ratings. It can be shown the linear regression model is      inapprpriate for this model.


NOTE:
1. In CRUD operations, the queries need to be given in JSON format.
2. A folder named 'static' needs to be created where visulaised graphs need to be stored in order for it to be displayed on main page.
3. All files and subfolders should be in the same directory.
4. The Data has been cleaned and necessary columns have been dropped and new data is stored in 'clean_data.csv'
5. To check availability of the ports and kill unecessary processes, use the following commands:
-> To find availability: netstat -ano|find ":<port number>"
-> Kill Process: taskkill /pid <process id> /f
