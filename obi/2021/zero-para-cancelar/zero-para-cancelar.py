qtd = int(input()) # Quantidade de números

numeros = []
for i in range(0, qtd):
  num = int(input())
  if num != 0:
    numeros.append(num)
  else:
    numeros.pop() # Se o número for 0, remove o último número adicionado

print(sum(numeros)) # Soma todos os números