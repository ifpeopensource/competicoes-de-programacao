N = int(input())
P = []
menor_preco = 0

for i in range(N):
    P.append(int(input()))

P.sort(reverse=True)

for i in range(0, len(P)):
    if i % 3 == 2:
        continue
    menor_preco += P[i]
print(menor_preco)
