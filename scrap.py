import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import csv


dic={'title':None,'content':None,'category':None,'url':None}

url=input("Enter the url:\t")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

dic['title']=soup.title.text
dic['content']=soup.text
dic['url']=url


import csv
l=[]
l.append(dic)
  
field_names = ['title', 'content', 'category','url']
  
with open('output.csv', 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
#     writer.writeheader()
    writer.writerows(l)

print('added Successfully')