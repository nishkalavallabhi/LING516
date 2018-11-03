from bottle import get, post, request, route, template, run
import re, string, collections

@route('/')
@route('/upload')
def uploadfile():
    html_code = '''<form action="/upload" method="post" enctype="multipart/form-data">
  Select a text file: <input type="file" name="upload" />
  <input type="submit" value="Upload file" />
</form>'''
    return html_code

@post('/upload')
def afterupload():
    uploaded_file = request.files.get('upload')
    if uploaded_file.filename.endswith(".txt"):
        uploaded_file.save("uploadedfile.txt", "w")
        #pre-processing
        text = open("uploadedfile.txt").read().lower().replace("\n"," ")
        newtext = re.sub('['+string.punctuation+']'," ",text)
        newtext = re.sub(" +"," ",newtext)
        all_words = newtext.strip().split(" ")

        counter = collections.Counter(all_words)
        #Prints type-token ratio
        ty_to = len(counter)/len(all_words)

        get1counts = collections.Counter(list(counter.values()))
        num1s = get1counts.most_common(1)[0][1]
        #percentage of words that appear only once (percentage of rare words)
        mean = (num1s/len(counter)*100)

        mostcommon25 = counter.most_common(25)
        totalfreqof25 = 0
        for tuple in mostcommon25:
            totalfreqof25 = totalfreqof25+tuple[1]
            #Average frequency of Top 25 words
            arw = totalfreqof25/25
        one = "The type-token ratio for this text is " + "{:.2}".format(ty_to)
        two = "The average frequency for the top 25 words is " + "{:.2}".format(mean)
        three = "The percentage of rare words is " + "{:.2}".format(arw)
        return one + "\n" + two + "\n" + three

    else:
        return "Wrong extension. Only .txt allowed"

run()
