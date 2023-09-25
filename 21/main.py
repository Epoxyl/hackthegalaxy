import json
import re

with open('countries.json') as f:
    countries = json.loads(f.read())

countries = countries["countries"]
words1 = ["sum", "sigma", "e", "five"]
words2 = ["flash", "lightning", "thunder", "flare", "blaze", "levin", "bolt", "streak", "stud", "stake", "volt"]
#words1 = ["cube", "quare"]
#words2 = ["nine"]

words = []
for word1 in words1:
    for word2 in words2:
        words.append(word1+word2)

for word in words:
    for country in countries:
        new_country = re.sub(r'[^A-Za-z]+', '', country.lower())
        if new_country in word:
            print("{} found in {}".format(new_country, word))
