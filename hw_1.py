# create class, clean punctuation and rewrite text file
import re
class TextCleaner:
    uncleanText = open('C:\Book.txt').read()
    cleanText = re.sub('[^A-Za-z0-9\s]+', '', uncleanText)
    open('C:\Book.txt', 'w').write(cleanText)

text=open('C:\Book.txt').read()
text = text.lower()


# create list of words
word_list=text.split()
print(word_list)

#text.close()
#create dictionary
d = {}

for word in word_list:
    d[word] = d.get(word,0) + 1

#count words
for key,val in d.items():
    print (key, val, 'times')


