roomCount = int(input())
peopleName = []
peopleFound = []

# handle input 
for i in range(roomCount):
  peopleName.append(str(input()))

peopleName = sorted(peopleName)

currentPerson = ''

def findMiddleAndCompare(newList):
  middleIndex = int(len(newList) - 1) // 2

  currentPerson = peopleName[middleIndex]
  if (currentPerson != 'Henrique'):
    if ord('H') > ord(list(currentPerson)[0]):
      findMiddleAndCompare(peopleName[middleIndex:(len(newList) - 1)])
    else:
      findMiddleAndCompare(peopleName[0:middleIndex])
  peopleFound.append(currentPerson)


findMiddleAndCompare(peopleName)

# print in reverse 
# can use reverse(peopleFound) too
for i in range((len(peopleFound) - 1), -1, -1):
  print(peopleFound[i])
