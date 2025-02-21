import requests
from bs4 import BeautifulSoup

URL = "https://www.cursbnr.ro/"

response = requests.get(URL)

parsed_page = BeautifulSoup(response.content, "html.parser")


valori =  parsed_page.find_all("div", {"class":"value"})
# print(valori)
for currency in valori:
    if "EURO" in currency.text and "Lei" in currency.text:
        print(currency.text)