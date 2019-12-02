import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_csv('C:/Users/niles/Desktop/DSR_BDA Project/googleplaystore.csv')

print('Different types of App Categories as present in the dataset are: ')
print('--------------------------------------------------------------------')

count = 1
for i in df['Category'].unique():
    print(count,': ',i)
    count = count + 1

df[df['Category'] == '1.9']
df.drop(df.index[[10472]],inplace = True) #incoreect data

#Plot 1: Number of Apps on the basis of category
sns.set_style('whitegrid')
plt.figure(figsize=(16,8))
plt.title('Plot 1: Number of apps on the basis of category')
sns.countplot(x='Category',data = df)
plt.xticks(rotation=90)
plt.show()


#Plot 2: Top 10 App categories
category = pd.DataFrame(df['Category'].value_counts())
category.rename(columns = {'Category':'Count'},inplace=True)
plt.figure(figsize=(15,6))
sns.barplot(x=category.index[:10], y ='Count',data = category[:10],palette='hls')
plt.title('Plot 2: Top 10 App categories')
plt.xticks(rotation=90)
plt.show()


family_category = len(df[df['Category'] == 'FAMILY'])/len(df)*100
games_category = len(df[df['Category'] == 'GAME'])/len(df)*100
beauty_category = len(df[df['Category'] == 'BEAUTY'])/len(df)*100
print('Percentage of Apps in the family category: {}%'.format(round(family_category,2)))
print('Percentage of Apps in the games category: {}%'.format(round(games_category,2)))
print('Percentage of Apps in the beauty category: {}%'.format(round(beauty_category,2)))


#Plot 3: Countplot For Ratings
plt.figure(figsize=(15,8))
sns.countplot(x='Rating',data = df)
plt.xticks(rotation =90)
plt.title('Plot 3: Countplot for ratings')
plt.show()


rating_greater_4 = len(df[df['Rating'] >= 4])/len(df)*100
print('Percentage of Apps having ratings of 4 or greater: {}%'.format(round(rating_greater_4,2)))


df['Size'] = df['Size'].apply(lambda x: str(x).replace('M',''))
df['Size'] = df['Size'].apply(lambda x: str(x).replace('k','e-3'))
#Converting the data type of Size category to float wherever possible
def convert(val):
    try:
        return float(val)
    except:
        return val
df['Size'] = df['Size'].apply(lambda x: convert(x))
#Seperate the apps whose size is given from those whose size varies with the device.
sized = df[df['Size'] != 'Varies with device'].copy()
sized['Size'] = pd.to_numeric(sized['Size'])



size_less_20 = len(sized[sized['Size'] <= 50 ])/len(sized)*100
print('Percentage of Apps in the beauty category: {}%'.format(round(size_less_20,2)))


#Plot 4: Number of apps on the basis of installs
order = ['0','0+','1+','5+','10+','50+','100+','500+','1,000+','5,000+','10,000+','50,000+','100,000+','500,000+','1,000,000+',
         '5,000,000+','10,000,000+',
         '50,000,000+','100,000,000+','500,000,000+','1,000,000,000+']
sns.set_style('whitegrid')
plt.figure(figsize=(22,8))
plt.title('Plot 4: Number of apps on the basis of Installs')
sns.countplot(x='Installs',data = df,palette='hls',order = order)
plt.xticks(rotation = 90)
plt.show()



print('{}% apps in the play store having more than 1,000,000 installs and {}% apps have more than 10,000,000+ downloads' .format(round(len(df[df['Installs'] == '1,000,000+'])/len(df)*100,2),round(len(df[df['Installs'] == '10,000,000+'])/len(df)*100,2)))



print('Apps on the basis of Type are classified as')
print('--------------------------------------------------------------------')

count = 1
for i in df['Type'].unique():
    print(count,': ',i)
    count = count + 1
plt.figure(figsize=(10,6))

# Data to plot
labels = ['Free','Paid']
sizes = [len(df[df['Type'] == 'Free']),len(df[df['Type'] == 'Paid'])]
colors = ['skyblue', 'yellowgreen','orange','gold']
explode = (0.1, 0)

# Plot 5: Percentage of Paid and Unpaid Apps
plt.title('Plot 5: Percentage of Free and paid apps in playstore')
plt.pie(sizes, labels=labels,
autopct='%1.1f%%', startangle=380,colors=colors,explode=explode)
plt.axis('equal')
plt.show()


df['Price'] = df['Price'].apply(lambda x: str(x).replace('$',''))
df['Price'] = pd.to_numeric(df['Price'])



print('Apps on the basis of Content Rating are classified as')
print('-------------------------------------------------------------------')

count = 1
for i in df['Content Rating'].unique():
    print(count,': ',i)
    count = count + 1


#Plot 6: Countplot Based on ratings
plt.figure(figsize=(12,6))
plt.title('Plot 6: Countplot Based on Content Ratings')
sns.countplot(x=df['Content Rating'],palette='hls')
plt.show()

print('Percentage of Apps having content rating as everyone: {}%'.format(round(len(df[df['Content Rating'] == 'Everyone'])/len(df)*100,2)))

#Plot 7: Countplot for number of apps in each Genre
plt.figure(figsize=(22,8))
plt.title('PLot 7: Number of Apps on the basis of Genre')
sns.countplot(x='Genres',data = df,palette='hls')
plt.xticks(rotation = 90)
plt.show()


print('Total Number of Genres: ',df['Genres'].nunique())


#Plot 8: Number of apps based on the Android Versions They require
plt.figure(figsize=(22,8))
plt.title('Plot 8: Number of Apps on the basis of Android version required to run them')
sns.countplot(x='Android Ver',data = df.sort_values(by = 'Android Ver'),palette='hls')
plt.xticks(rotation = 90)
plt.show()


#function to convert columns to numeric data type from object data type
for i in df.columns:
    try:
        df[i] = pd.to_numeric(df[i])
    except:
        pass


#Plot 9: App ratings in each Category
plt.figure(figsize=(20,6))
sns.boxplot(x='Category',y='Rating',data = df)
plt.xticks(rotation=90)
plt.title('Plot 9: App ratings across different categories')
plt.show()



#Plot 10: Reviews in Each Category
sns.set_style('whitegrid')
plt.figure(figsize=(15,8))
sns.scatterplot(y='Category',x='Reviews',data = df,hue='Category',legend=False)
plt.xticks(rotation=90)
plt.title('Number of reviews on the basis of Category')
plt.show()
