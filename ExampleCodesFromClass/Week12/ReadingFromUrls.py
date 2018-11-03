'''
This python file is a collection of functions that illustrate different ways of accessing and parsing the contents in a URL.
Depending on what the nature of the url is (text, image, html etc.), there are some differences in the way we use the same functionality.
Please go through these examples, understand what is the difference between different versions that read the same url.
'''

import urllib.request

#Reading from a URL which is a .txt file. 
def readTextFileUrl():
    fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
    for line in fhand:
        print(line.strip())
    fhand.close()

#Reading from a URL which is a .txt file - What is the difference between the function above this and this?
def readTextFileUrl2():
     fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
     for line in fhand:
        print(line.decode(encoding="UTF-8").strip())
#If you don't decode here, you will see byte strings, and not actual strings on which you can use string methods.

#Reading from a URL which is a .html file.
def readHtml():
    fhand = urllib.request.urlopen('http://apling.engl.iastate.edu')
    for line in fhand:
       print(line.decode(encoding="utf8").strip())
#This will print HTML code line by line

#Reading from a URL which is a image file. This function will print the byte stream of the image line by line
def readImageFileUrl():
    fhand = urllib.request.urlopen('http://www.phdcomics.com/comics/archive/phd031813s.gif')
    for line in fhand:
         print(line)

#Reading from a URL which is a image file. This function will download the image and save it in a local temp folder.
#Note that this uses urlretrieve() and not urlopen(). What is the difference? Search and find out.
def readImageFileUrl2():
    fhand = urllib.request.urlretrieve('http://www.phdcomics.com/'
                                       'comics/archive/phd031813s.gif')
    for line in fhand:
         print(line)

#Read a image file, and save it locally, wherever you want, under whatever name you want.
#Note the "wb" there. What does that mean? Seach and find out.
def saveImageUrl():
    img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()
    fhand = open('cover2.jpg', 'wb')
    fhand.write(img)
    fhand.close()


#To test all the above methods, uncomment the function calls below, one at a time and check the output. 

#readTextFileUrl()
#readTextFileUrl2()
#readImageFileUrl()
#readImageFileUrl2()
#readHtml()
#saveImageUrl()
