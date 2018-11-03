txt = "but soft what light in yonder window breaks"
words = txt.split()
t = list()
for word in words:
  t.append((len(word), word))
print("Here is that string with the word length, and the word tuple pairs:")
print(t)
t.sort(reverse=True)
res = list()
for length, word in t:
  res.append(word)
print("Here is the list of words in the String sorted by their length")
print(res)
