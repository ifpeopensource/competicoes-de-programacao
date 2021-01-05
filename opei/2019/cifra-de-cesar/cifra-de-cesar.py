shift = int(input())
message = str(input())
result = []

for index, char in enumerate(message):
  result.append(chr(ord(message[index]) - shift))

resultParsed = ''.join(char for char in result)
print(resultParsed)

