from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


mongo_client=MongoClient()
db=mongo_client.testdb


#Query1:Number of Paid and Free apps based on category
query = {"Type":"Paid"}
df = pd.DataFrame(db.testcollection.find(query))
sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
plt.title('Number of Paid apps on the basis of category')
sns.countplot(x='Category',data = df)
plt.xticks(rotation=90)
#plt.show()
plt.savefig("<PATH>/im1.png")

query = {"Type":"Free"}
df = pd.DataFrame(db.testcollection.find(query))
sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
plt.title('Number of Free apps on the basis of category')
sns.countplot(x='Category',data = df)
plt.xticks(rotation=90)
#plt.show()
plt.savefig("<PATH>/im2.png")


#Query2:Number of apps having rating less than 3.0 in each Genre
query =  { "Rating": { "$lt": "3.0" } }
df = pd.DataFrame(db.testcollection.find(query))
df = df.dropna()
print(df[['Rating']])
sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
plt.title('Number of apps of Rating <3.0 Genre wise')
sns.countplot(x='Genres',data = df)
plt.xticks(rotation=90)
#plt.show()
plt.savefig("<PATH>/im3.png")


#Query 3:Scatterplot of category v/s reviews for Teens
query = {'Content Rating':'Teen'}
df = pd.DataFrame(db.testcollection.find(query))
for i in df.columns:
    try:
        df[i] = pd.to_numeric(df[i])
    except:
        pass
sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
sns.scatterplot(x='Category',y='Reviews',data = df,hue='Category',legend=False)
plt.xticks(rotation=90)
plt.title('Category V/S Reviews for Apps Developed for teens')
#plt.show()
plt.savefig("<PATH>/im4.png")


#Query 4:Pie chart for paid and free tool apps
query = {'Genres':'Tools'}
df = pd.DataFrame(db.testcollection.find(query))
count = 1
for i in df['Type'].unique():
    print(count,': ',i)
    count = count + 1
plt.figure(figsize=(8,8))
labels = ['Free','Paid']
sizes = [len(df[df['Type'] == 'Free']),len(df[df['Type'] == 'Paid'])]
colors = ['skyblue', 'yellowgreen','orange','gold']
explode = (0.1, 0)
plt.title('Percentage of Free and paid Tool apps')
plt.pie(sizes, labels=labels,
autopct='%1.1f%%', startangle=380,colors=colors,explode=explode)
plt.axis('equal')
#plt.show()
plt.savefig("<PATH>/im5.png")


#Query 5:Bar graph to show competitors in a Category
query = {"Category":"SHOPPING"}
df = pd.DataFrame(db.cleandata.find(query).sort("Installs",-1).limit(10))
df["Installs"] = pd.to_numeric(df["Installs"])
sns.set_style('whitegrid')
plt.figure(figsize=(8,8))
sns.barplot(y='Installs',x='App',hue='App',data=df)
plt.legend().set_visible(False)
plt.title('Top Competitors based on Installs in Shopping Category')
plt.xticks(rotation=90)
plt.savefig("<PATH>/im6.png")


#Query 6: To show paid apps have better ratings
df = pd.DataFrame(db.cleandata.find())
for i in df.columns:
    try:
        df[i] = pd.to_numeric(df[i])
    except:
        pass
plt.figure(figsize=(8,8))
sns.boxplot(x='Type',y='Rating',data = df)
plt.xticks(rotation=90)
plt.title('Comparison of Rating of Paid and Free Apps')
plt.savefig("<PATH>/im7.png")
