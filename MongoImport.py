import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C:/Users/niles/Desktop/DSR_BDA Project/clean_data.csv', 'r', encoding="utf-8")
reader = csv.DictReader( csvfile )
mongo_client=MongoClient()
db=mongo_client.testdb
db.cleandata.drop()
header= [ "App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    db.cleandata.insert(row)
