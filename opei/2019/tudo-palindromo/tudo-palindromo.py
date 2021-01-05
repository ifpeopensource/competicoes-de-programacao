listString = list(input().replace(" ", ""))
# made convertion with list() typecasting
# alternatively we could do:
# listString = char for char in word
# also removed all whitespace with replace() method

ocurrences = {}
# add ocurrences in dict
for char in listString:
  if char not in ocurrences:
    ocurrences[char] = 1
  else:
    ocurrences[char] += 1
    

removes = 0
# to iterate an object (dict)
for i in ocurrences.keys():
  if (ocurrences[i] % 2) != 0:
    removes += 1

# Check if it's possible to have just only one char in the middle of string
if (len(listString) - removes + 1) % 2 != 0:
  removes -= 1

print(removes)
