import urllib.request
from bs4 import BeautifulSoup
import webbrowser

class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)

        file = open("D:\Projects\GoogleNewsScraper\GNScraperOut.txt","r+")
        file.truncate() #clears contents of the output file before updating
        file = file.close()

        file = open("D:\Projects\GoogleNewsScraper\GNScraperOut.txt","a+")
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                file.write(url + "\r\n")
        file = file.close()

news = "https://news.google.com/"
Scraper(news).scrape()

lines_seen = set()
outfile = open("D:\Projects\GoogleNewsScraper\GNScraperDeDuped.txt","w")
for line in open("D:\Projects\GoogleNewsScraper\GNScraperOut.txt","r"):
    if line != "\n":
        if line not in lines_seen:
            outfile.write(line + "\n")
            lines_seen.add(line)
outfile.close()

webbrowser.open("D:\Projects\GoogleNewsScraper\GNScraperDeDuped.txt")