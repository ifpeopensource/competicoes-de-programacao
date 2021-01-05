peopleCount = int(input())

sumDesks = 0

while peopleCount > 0:
  if sumDesks > 0:
    # when you add another desk, you earn 3 new places but lose one (3 -1 = 2)
    peopleCount -= 2
  else:
    peopleCount -= 4
  sumDesks += 1

print(sumDesks)