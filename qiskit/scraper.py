import html5lib
from bs4 import BeautifulSoup
import requests

class scraper:
    def __init__(self, startPage, endPage):
        self.startPage = startPage
        self.endPage = endPage
    
    def scrapeArticle(self, url):
        response = requests.get(url = url,)
        soup = BeautifulSoup(response.content, 'html5lib')
        title = soup.find(id = "firstHeading")
        allLinks = soup.find(id = "bodyContent").find_all("a")
        return allLinks