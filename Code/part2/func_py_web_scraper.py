# func_py_web_scraper.py
import requests
from bs4 import BeautifulSoup

def func_py_web_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    return "Failed to fetch page"

print(func_py_web_scraper("https://example.com"))
