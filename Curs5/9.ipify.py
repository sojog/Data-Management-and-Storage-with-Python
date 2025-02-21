import requests
from bs4 import BeautifulSoup

URL = "https://api.ipify.org/"

response = requests.get(URL)

parsed_page = BeautifulSoup(response.content, "html.parser")

print(parsed_page, type(parsed_page))
