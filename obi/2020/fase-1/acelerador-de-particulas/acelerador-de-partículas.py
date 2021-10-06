distancia = int(input())

distancia -= 3 # Subtrai a distância até chegar no acelerador
distancia %= 8 # Encontra a distância percorrida na última volta

distancia -= 2 # Subtrai a distância percorrida até o primeiro sensor
print(distancia)

# O código poderia ser escrito de forma bem mais simplificada:
# print(((int(input()) - 3) % 8) - 2)
