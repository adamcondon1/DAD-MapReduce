#imports for algebra and data processing 
import numpy as np 
import pandas as pd 
import matplotlib as plt

#Directory to files
import os
for dirname, _, filenames in os.walk('\DAD CA2\VGSalesRecords'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('vgsales.csv')
df

#Gathering relevant columns to preform analysis and retriev the relevant info needed
global_publishers = df['Publisher']
most_common_publisher = global_publishers.mode()
most_common_publisher

platforms = df['Platform']
most_common_platform = platforms.mode()
most_common_platform

genres = df['Genre']
most_common_genre = genres.mode()
most_common_genre

top_twenty_grossing = df.nlargest(20, ['Global_Sales'])
top_twenty_grossing

#Finding the median using algebra import
m = df['NA_Sales'].median()
print('Median:', m)

#Finding highest values for Global Sales
highest_sales = df.nlargest(1,['Global_Sales'])
highest_sales

#Finding NA sales mean (Average)
na_sales_std = df["NA_Sales"].std()
print('NA Std:', na_sales_std)
na_sales_mean = df["NA_Sales"].mean()
print('NA Mean:', na_sales_mean)

#Finding the highest NA Sales
highest_sales_na = highest_sales["NA_Sales"]
distance_from_mean = abs(na_sales_mean - highest_sales_na)
print("Distance From Mean:",distance_from_mean)
num_std_from_mean = distance_from_mean / na_sales_std
print("Standard Deviations Away From The Mean:", num_std_from_mean)

wii_games = df[df["Platform"] == "Wii"]
wii_games

#Mean of Wii games
wii_avg = wii_games["Global_Sales"].mean()
print("Average Sales For Wii Games:",wii_avg)
other_platforms = df[df["Platform"] != "Wii"]
others_avg = other_platforms["Global_Sales"].mean()
print("Average Sales For All Other Platforms:",others_avg)

years = df['Year']
most_recent_in_data = years.max()
most_recent_in_data

platforms = df.Platform.unique()
platforms

genres = df.Genre.unique()
genres

years = df.Year.unique()
years