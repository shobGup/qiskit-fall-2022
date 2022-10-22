import requests
from bs4 import BeautifulSoup

class scraper:
    def __init__(self, startPage, endPage):
        self.startPage = startPage
        self.endPage = endPage
        self.graph = {}
    
    def scrapeArticle(self, url):
        response = requests.get(url = url,)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id = "firstHeading")
        allLinks = soup.find(id = "bodyContent").find_all("a").find("/wiki/")
        self.graph[title] = allLinks
    
