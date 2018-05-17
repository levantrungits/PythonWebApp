__author__="trunglv"

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/2018-apple-ipad-9-7-inch-a10-ios-11-wi-fi-32gb/p2999393")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip() # "£319.00"

price_without_symbol = string_price[1:] # "319.00"

price = float(price_without_symbol)
print("The current price is {}".format(string_price))

if price < 200:
    print("You should buy the chair!")
else:
    print("Do not buy, it's too expensive!")
