#camisetas - OBI 2020
count1 = 0
count2 = 0


n = int(input()) # total de premiados
T = [int(i) for i in input().split()] # cada tamanho
if len(T) == n:
  p = int(input()) # total de tamanho p
  m = int(input()) # total de tamanho m
else: 
  print("falso")

for i in range(len(T)):
  if T[i] == 1:
    count1+=1
  if T[i] == 2:
    count2 += 1
  
if (count1 == p) & (count2 == m):
  print("S")
else:
  print("N")


