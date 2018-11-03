#Example code to parse XML in python using Beautiful Soup.

from bs4 import BeautifulSoup

def parseXMLLikeContentWithSoup():
   content = BeautifulSoup(open("xml-example2.xml").read(),"html.parser")
   m2Tag = "methods_m2_describing_study"
   allM2tags = content.find_all(m2Tag)
   for i in range(0,len(allM2tags)):
      if allM2tags[i].get("step") == "describing_data":
         print(allM2tags[i].get_text())

parseXMLLikeContentWithSoup()