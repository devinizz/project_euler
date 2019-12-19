P = []
L = list(range(1000001))
for i in range(2, len(L)):
  if L[i] == i:
    P.append(i)
    L[i] = i - 1
  for p in P:
    if i * p >= len(L):
      break
    if i % p == 0:
      L[i*p] = L[i] * p
      break
    L[i*p] = L[i] * (p - 1)

L[1] = 0
print(sum(L))
