import requests
from bs4 import BeautifulSoup

def get_upper(_item_):
    return _item_.upper()

def get_url(from_curr:str, to_curr:str) -> str:
    return f"https://www.google.com/finance/quote/{from_curr}-{to_curr}?hl=en"


def get_price(from_curr:str, to_curr:str, class_html="AHmHk"):

    page = requests.get(get_url(from_curr,to_curr))
    price = BeautifulSoup(page.content, "html.parser").find("div", {"class":{class_html}}).text
    price = float(price)
    
    return price


def get_exchange_rate(from_curr:str, to_curr:str) -> str:

    from_curr, to_curr = utils.get_upper(from_curr), utils.get_upper(to_curr)

    try:
        exchange_rate = utils.get_price(from_curr,to_curr)

    except RuntimeError as err:
        raise RuntimeError(
            "Please check the currency symbols. If they're right, wait for a few minute to reperforme the code"
                           ) from err 
    
    return exchange_rate