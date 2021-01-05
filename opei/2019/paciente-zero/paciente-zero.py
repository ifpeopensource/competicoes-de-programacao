pacientsCount = int(input())

badPacients = []
infectedPacients = []

# handle input
for i in range(pacientsCount):
  inputLine = input().split()

  currentBadPacientName = inputLine[0]
  if currentBadPacientName not in badPacients:
    badPacients.append(currentBadPacientName)

  infectedCount = int(inputLine[1])
  if (infectedCount > 0):
    # good for handling not-known inline inputs
    currentInfectedPacients = inputLine[2:len(inputLine)]
    for pacient in currentInfectedPacients:
      if pacient not in infectedPacients:
        infectedPacients.append(pacient)

for pacient in badPacients:
  if pacient not in infectedPacients:
    print(pacient)
