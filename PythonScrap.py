#Oucema and oumayma 
import requests
from bs4 import BeautifulSoup
import csv 
# URL for scraping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
 
# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
 
data = []
 
# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))
 
# data_iterator is the iterator of the table
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
 
        # For 'confirmed' and 'deaths',
        data.append((
            country,
            int(confirmed.replace(',','')),
            int(deaths.replace(',','')),
            continent
        ))
 
    # StopIteration error is raised when
    # there are no more elements left to
    # iterate through
    except StopIteration:
        break
 
# Sort the data by the number of confirmed cases
data.sort(key = lambda row: row[1], reverse = True)

import texttable as tt
table = tt.Texttable()
 
# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + data)
 
# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c')) 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))
 
print(table.draw()) 






with open ("SCRAPING_COVID19.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(data)