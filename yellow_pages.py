from urllib import request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url="http://yellowpages.in/hyderabad/food-and-beverages/606286653"
response = requests.get(url)
# print(response.status_code)

soup=BeautifulSoup(response.text,'lxml')
# print(soup)

fbt = soup.find_all('div',class_="eachPopular")
# print(fbt)
binfo =[]

for t in fbt:
    titles =t.find('div', class_="popularTitleTextBlock").text.replace('/n' ,'')
    # print(titles)
    contact =t.find('a',class_="businessContact").text.replace('/n' ,'')
    # print(contact)
    images= t.img['src']
    
    links= t.find('a')
    l =links['href']
    bl = "https://www.http://yellowpages.in/hyderabad/food-and-beverages"
    bli = bl+l
    # print(bli)
    
    
    contact_dictionary = {'Business_Name': titles, 
    'Bcontact':contact,'Image_link': images, 'Business_Links' : bli }


    binfo.append(contact_dictionary)

    # print(binfo)

    binfo_df = pd.DataFrame(binfo)

    binfo_df.to_csv('Binfo.csv',index = None)
