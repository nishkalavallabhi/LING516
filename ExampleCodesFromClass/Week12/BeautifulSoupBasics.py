#Demo code to show how to work with Beautiful Soup

import urllib.request
from urllib import request
from bs4 import BeautifulSoup

#Get the footer of the given webpage. This assumes all webpages have this footer.
def getFooter(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('div')
    for tag in tags:
        span_class=tag.get("class")
        #print(span_class)
        if  span_class and span_class[0].lower() == "wd-l-pagefooter": #this contains footer
          print(tag.text.strip())

def getCustom(url,htmltag):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup(htmltag)
    for tag in tags:
        print(tag)

#URLs in any HTML are represented in a tag that is called "a" and within a, in a field called "href"
def getAllUrls(url):
    url_content = request.urlopen(url).read()
    soup = BeautifulSoup(url_content,"html.parser")
    tags = soup("a")
    for tag in tags:
        url = tag.get("href", None)
        if isinstance(url,str):
            if url.startswith("http"):
                print(url)

url1 = "http://apling.engl.iastate.edu"
#getCustom(url1,"li")
#De-comment one of them to see how it works.
#getFooter(url1)
getAllUrls(url1)

#Extra: Change where appropriate, to return all URLs as a list instead of printing them directly, and
# count the total number of urls
# total number of urls coming from .iastate.edu domain, and those coming from outside.
