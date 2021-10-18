# OBI 2020 - Tres por Dois

quantidade = int(input())
preco = []
total = 0
for n in range(quantidade):
    preco.append(int(input()))

preco.sort(reverse=True)

for n in range(0, len(preco)):
    if n % 3 == 2:
        continue
    total += preco[n]

print(total)
