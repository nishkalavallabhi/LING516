import re,string,collections

#pre-processing
text = open("enemy.txt").read().lower().replace("\n"," ")
newtext = re.sub('['+string.punctuation+']'," ",text)
newtext = re.sub(" +"," ",newtext)
all_words = newtext.strip().split(" ")

counter = collections.Counter(all_words)

#Prints type-token ratio
#print(len(counter)/len(all_words))

get1counts = collections.Counter(list(counter.values()))


num1s = get1counts.most_common(1)[0][1]
#percentage of words that appear only once (percentage of rare words)
print(num1s/len(counter)*100)

mostcommon25 = counter.most_common(25)
totalfreqof25 = 0
for tuple in mostcommon25:
    totalfreqof25 = totalfreqof25+tuple[1]
#Average frequency of Top 25 words
print(totalfreqof25/25)
