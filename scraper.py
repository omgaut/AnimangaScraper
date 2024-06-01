# Code to scrape the Big 3 Anime's Episode to Manga Conversions, and format into CSV file

from bs4 import BeautifulSoup
import pandas as pd
import requests

#Create URL object
url = 'https://listfist.com/list-of-one-piece-episode-to-chapter-conversion'
url2 = 'https://listfist.com/list-of-bleach-episode-to-chapter-conversion'
url3 = 'https://listfist.com/list-of-naruto-episode-to-chapter-conversion'
url4 = 'https://listfist.com/list-of-naruto-shippuden-episode-to-chapter-conversion'

#Create object page
page = requests.get(url)
page2 = requests.get(url2)
page3 = requests.get(url3)
page4 = requests.get(url4)

soup = BeautifulSoup(page.text, 'lxml')
soup2 = BeautifulSoup(page2.text, 'lxml')
soup3 = BeautifulSoup(page3.text, 'lxml')
soup4 = BeautifulSoup(page4.text, 'lxml')

# Obtain information from tag <table>
table1 = soup.find("table", id="igsv-1mGtvb_1HownoAPQt3NftgtB7fM96toIQ8UnnwpNnJcs")
table2 = soup2.find("table", id="igsv-15BLf9AkJpWkoMt5jBLk0mosIMSJxux7V5d3Hxdyltss")
table3 = soup3.find("table", id="igsv-1vrSJmOVjxkYQhT3gYa0Je9TyD0hVbWmdG5PzDh3SnuQ")
table4 = soup4.find("table", id="igsv-1vrSJmOVjxkYQhT3gYa0Je9TyD0hVbWmdG5PzDh3SnuQ")


# One Piece Scraping
# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all("th"):
 title = i.text
 headers.append(title)

# Renaiming headers
headers[0] = "Episode"
headers[2] = "Manga Chapter"

data = pd.DataFrame(columns = headers)

# Create a for loop to fill mydata
for j in table1.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data)
 data.loc[length] = row

 data.to_csv("data1.csv", index=False)

# Deleting Title Column
d = pd.read_csv("data1.csv")
del d["Title"]
d.to_csv("onepiece_data.csv",index=False)

# Bleach Scraping
# Obtain every title of columns with tag <th>
headers2 = []
for i in table2.find_all("th"):
 title = i.text
 headers2.append(title)

# Renaiming headers
headers2[0] = "Episode"
headers2[2] = "Manga Chapter"

data2 = pd.DataFrame(columns = headers2)

# Create a for loop to fill mydata
for j in table2.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data2)
 data2.loc[length] = row

 data2.to_csv("data2.csv", index=False)

# Deleting Title Column
d = pd.read_csv("data2.csv")
del d["Title"]
d.to_csv("bleach_data.csv",index=False)

# Naruto Scraping
# Obtain every title of columns with tag <th>
headers3 = []
for i in table3.find_all("th"):
 title = i.text
 headers3.append(title)

# Renaiming headers
headers3[0] = "Episode"
headers3[2] = "Manga Chapter"

data3 = pd.DataFrame(columns = headers3)

# Create a for loop to fill mydata
for j in table3.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data3)
 data3.loc[length] = row

 data3.to_csv("data3.csv", index=False)

# Deleting Title Column
d = pd.read_csv("data3.csv")
del d["Title"]
d.to_csv("naruto_data.csv",index=False)

# Naruto Shippuden Scraping
# Obtain every title of columns with tag <th>
headers4 = []
for i in table4.find_all("th"):
 title = i.text
 headers4.append(title)

# Renaming headers
headers4[0] = "Episode"
headers4[2] = "Manga Chapter"

data4 = pd.DataFrame(columns = headers4)

# Create a for loop to fill mydata
for j in table4.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data4)
 data4.loc[length] = row

 data4.to_csv("data4.csv", index=False)

# Deleting Title Column
d = pd.read_csv("data4.csv")
del d["Title"]
d.to_csv("narutoshippuden_data.csv",index=False)