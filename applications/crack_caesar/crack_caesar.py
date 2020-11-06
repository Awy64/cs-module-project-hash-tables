# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re #import regex

with open("ciphertext.txt") as f: #open file and make is a string
  words = f.read()

letter = re.findall("[A-Z]", words) # filter only letters
total = {} # create a dict to store totals of each letter
for i in letter: # count each letter and add the count to the dict
  if i in total:
    total[i] += 1
  else:
    total[i] = 1
sort = sorted(total, key=total.get, reverse=True) #create a sorted list baised on the key values reversed.
most = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', # added most used letters on avg.
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
count = 0
for i in sort: #convert dict to a cypher by replacing the values in order with the same order as most common letters.
  total[i] = most[count]
  count += 1
new = list(words) # make the letters in the string mutable
for i in range(len(new)): # replace the letters with the dict that i snoy a cypher
  if new[i] in total:
    new[i] = total[new[i]]
new = "".join(new)

print(new) #display the decyphers text

