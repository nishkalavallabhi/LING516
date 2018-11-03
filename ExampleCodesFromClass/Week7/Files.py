

fhand = open("/home/bangaru/PycharmProjects/516Spring18/Week6/listdemo.py")
content = fhand.read()
str = content.split("\n")
for item in str:
    print(item)
