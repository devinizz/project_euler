from math import gcd

L = [0] * 1500001
for n in range(1, int(len(L) ** 0.5) // 2):
  for m in range(n + 1, 999999999999999999999, 2):
    if gcd(m, n) != 1:
      continue
    l = (m + n) * m * 2
    if l > len(L):
      break
    for i in range(l, len(L), l):
      L[i] += 1

print(sum(filter(lambda x: x == 1, L)))
