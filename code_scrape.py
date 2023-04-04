from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv
import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
cursor.execute("drop table theverge")
cursor.execute("create table theverge(id integer,url text,headline text,author text,date text)")
req = Request("https://www.theverge.com/")
html_page = urlopen(req)
soup = BeautifulSoup(html_page,"lxml")
headlines = soup.find_all(attrs={"class": ["group-hover:shadow-highlight-blurple","group-hover:shadow-underline-franklin","text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8","text-gray-63 dark:text-gray-94"]})
header = ['id','url','headline','author','date']
list=[]
with open('ddmmyyy_verge.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(0,6):
        j=i;
        i*=3
        record=[j,"https://www.theverge.com"+headlines[i].get("href"),headlines[i].text,headlines[i+1].text,headlines[i+2].text]
        row=(j,"https://www.theverge.com"+headlines[i].get("href"),headlines[i].text,headlines[i+1].text,headlines[i+2].text)
        list.append(row)
        writer.writerow(record)
cursor.executemany("insert into theverge(id,url,headline,author,date) values(?,?,?,?,?)",list)

connection.close()
