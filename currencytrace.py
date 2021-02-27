import requests
from bs4 import BeautifulSoup as bs
response = requests.get("https://www.doviz.com/")
soup = bs(response.content,"html.parser")
keys = soup.find_all("span",{"class":"name"})
values = soup.find_all("span",{"class":"value"})
