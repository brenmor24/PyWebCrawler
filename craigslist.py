import requests
from bs4 import BeautifulSoup

page = requests.get('https://chicago.craigslist.org/search/cla?query=air+force+one')
soup = BeautifulSoup(page.content,'html.parser')
listings = soup.find_all('li',{'class':'result-row'})
for listing in listings:
    print(listing.div.h2.a.text)

