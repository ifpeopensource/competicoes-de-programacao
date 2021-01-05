idCount = int(input())
idList = []

# handle input
for i in range(idCount):
  currentId = int(input())
  
  if currentId not in idList:
    idList.append(currentId)

print(len(idList))