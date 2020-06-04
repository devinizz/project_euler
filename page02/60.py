from prime import Prime
from miller_test import isPrime

def memory(n):
  m = dict()
  def mem(x):
    if x not in m:
      m[x] = isPrime(int(str(n) + str(x)), 10) and isPrime(int(str(x) + str(n)), 10)
    return m[x]
  return mem

clique = list(map(lambda x: list(), range(6))) 
clique[5].append([])
ans = 999999999
for p in Prime.prime():
  if p > ans:
    break
  mem = memory(p)
  for i in range(1, 6):
    if p * i > ans:
      break
    for s in clique[i]:
      if len(list(filter(mem, s))) == len(s):
        clique[i - 1].append(list(s) + [p])
  if len(clique[0]) > 0:
    ans = min(ans, min(map(sum, clique[0])))

print(ans)
