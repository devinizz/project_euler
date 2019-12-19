P = []
L = list(range(10000000))
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

print(min(map(lambda x: [x[0] / x[1], x[0]], filter(lambda x: sorted(str(x[0])) == sorted(str(x[1])), list(enumerate(L))[2:])))[1])
