import urllib.request
imagepath = "http://www.phdcomics.com/comics/archive/phd031813s.gif"
fhand = urllib.request.urlopen(imagepath)
for line in fhand:
    print(line)
