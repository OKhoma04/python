import re
# create class, clean punctuation and rewrite text file
class TextCleaner:
    uncleanText = open('C:\Book.txt').read()
    cleanText = re.sub('[^A-Za-z0-9\s]+', '', uncleanText)
    open('C:\Book.txt', 'w').write(cleanText)
# create function, replace values due to dictionary
def replace_words(base_text, device_values):
    for key, val in device_values.items():
        base_text = base_text.replace(key, val)
    return base_text

# create dictionary, replace roman numerals to int
device = {"ACT V":"ACT 5", "ACT IV":"ACT 4", "ACT III":"ACT 3", "ACT II":"ACT 2", "ACT I":"ACT 1"}

# Open desired file as 't' and read the lines into string 'tempstr'
t = open('C:\Book.txt', 'r')
tempstr = t.read()
t.close()

# replacement and lower case
output = replace_words(tempstr, device)
output = output.lower()

# write out the new file
fout = open('output.txt', 'w')
fout.write(output)
fout.close()

# create list of words
word_list=output.split()
print(word_list)

#create dictionary
d = {}

for word in word_list:
    d[word] = d.get(word,0) + 1

#count words
for key,val in d.items():
    print (key, val, 'times')
