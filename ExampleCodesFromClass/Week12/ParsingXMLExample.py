#Example code to parse XML in python using built in Python modules.

import xml.etree.ElementTree as AB

def parseXML1():
    xml_tree = AB.parse("xml-example.xml")
    #If I know that the first child of the xml root is "message"
    #and message has an attribute "href".
    print(xml_tree.getroot()[0].get("href"))

    #If I know that there is a "kudos" under "message" tag, and I want to search for something in it.
    print(xml_tree.getroot().find("message/kudos")[0].text) #use findall() if there can be multiple kudos.

    #To check if there are more kudos:
    kudos_list = xml_tree.getroot().findall("message/kudos")
    if len(kudos_list) > 1:
        print("there are more kudos elements")
    else:
        print("there is at max, one kudos element")

parseXML1()