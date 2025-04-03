import requests
from bs4 import BeautifulSoup

def fetch_stock_price(ticker):
    search_url = f"https://www.google.com/search?q={ticker}+stock+price"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    stock_price = extract_stock_price(soup)
    return stock_price

def extract_stock_price(soup):
    try:
        price_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        if price_element:
            return price_element.text
        else:
            return "Price not found"
    except Exception as e:
        return f"Error: {e}"