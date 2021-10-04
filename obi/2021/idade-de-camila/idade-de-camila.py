a = int(input()) # Idade da primeira irmã
b = int(input()) # Idade da segunda irmã
c = int(input()) # Idade da terceira irmã

idades = [a, b, c]
idades.remove(min(idades)) # Remove a menor idade
idades.remove(max(idades)) # Remove a maior idade

print(idades[0])