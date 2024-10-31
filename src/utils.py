import requests
from bs4 import BeautifulSoup

def get_upper(_item_):
    return _item_.upper()

def get_url(from_curr:str, to_curr:str) -> str:
    return f"https://www.google.com/finance/quote/{from_curr}-{to_curr}?hl=en"


def get_price(from_curr:str, to_curr:str, class_html="AHmHk"):

    page = requests.get(get_url(from_curr,to_curr))
    price = BeautifulSoup(page.content, "html.parser").find("div", {"class":{class_html}}).text

    return price
