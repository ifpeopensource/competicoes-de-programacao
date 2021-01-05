# matriz: N x M (N = altura, M = largura; N = y, M = x)
height, width = [int(number) for number in input().split()]
matrix = []
mainSum = 0

# Handle input
for i in range(height):
  matrix.append(input().split())
  for number in matrix[i]:
    number = int(number)

# Auxiliary function
def getRightLineSum(y, x):
  sum = 0
  for i in range(x, width):
    sum += int(matrix[y][i])
  return sum

# Auxiliary function
def getDownColumnSum(y, x):
  sum = 0
  for i in range(y, height):
    sum += int(matrix[i][x])
  return sum

# Main recursive function to find turns potential to increase mainSum
def findPotential(y, x):
  global mainSum

  turnRightPotential = 0
  turnDownPotential = 0

  turnRightCellsCount = 0
  turnDownCellsCount = 0

  if (y < height) and (x < width):

    mainSum += int(matrix[y][x])
    # print(matrix[y][x])

    # get turn right potential (x + 1)
    for i in range(y, height):
      turnRightPotential += getRightLineSum(i, x + 1)
      turnRightCellsCount += (width - x) 

    # get turn down potential (y + 1)
    for i in range(y + 1, height):
      turnDownPotential += getRightLineSum(i, x)
      turnDownCellsCount += (width - x - 1)

    turnDownAvrgPotential = (turnDownPotential / turnDownCellsCount) if (turnDownCellsCount > 0) else (turnDownPotential)
    turnRightAvrgPotential = (turnRightPotential / turnRightCellsCount) if (turnRightCellsCount > 0) else (turnRightPotential)

    if turnRightAvrgPotential >= turnDownAvrgPotential:
      findPotential(y, x + 1)
    else:
      findPotential(y + 1, x)

findPotential(0, 0)

print(mainSum)