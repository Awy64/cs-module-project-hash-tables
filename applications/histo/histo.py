# Your code here
import re

with open("robin.txt") as f:
    words = f.read()
words = words.casefold()
word = re.findall("(\w+)", words)
wordDict = {}
for a in word:
    if a not in wordDict:
        wordDict[a] = 1
    else:
        wordDict[a] += 1

# for w in sorted(wordDict, key=wordDict.get, reverse=True):
#     print(w, d[w])
string = "#"
for a in sorted(wordDict, key=wordDict.get, reverse=True):
    print("%-20s %s" % (a, string * wordDict[a]))