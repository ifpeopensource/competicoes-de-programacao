numero_do_cartão = [int(charNumber) for charNumber in list(input())]

def getNumberDigitsSum(number):
  sum = 0
  while number != 0:
    sum = sum + (number % 10)
    number = number // 10
  return sum

alternate = False
i = len(numero_do_cartão) - 1

while i >= 0:
  if alternate == True:
    new_number = numero_do_cartão[i] * 2
    if new_number >= 10:
      new_number = getNumberDigitsSum(new_number)
    numero_do_cartão[i] = new_number
  alternate = not alternate
  i -= 1

sum = 0
for number in numero_do_cartão:
  sum += number

if (sum % 10) == 0:
  print("SIM")
else:
  print("NAO")

