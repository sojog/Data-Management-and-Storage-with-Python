import requests
from bs4 import BeautifulSoup

URL = "https://icanhazdadjoke.com/"

response = requests.get(URL)

parsed_page = BeautifulSoup(response.content, "html.parser")

# print(parsed_page, type(parsed_page))
paragrafe =  parsed_page.find_all("p", {"class":"subtitle"})
# print(paragrafe)

joke = paragrafe[0]
# print(joke)
print(joke.text)