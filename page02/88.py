mem = []
used = set()
k = set(range(2, 12001))
for n in range(9999999999999999):
  mem.append(set())
  if len(k) == 0:
    break
  for p in range(2, 999999999999999999999):
    if p * p > n:
      break
    if n % p != 0:
      continue
    d = n // p
    for i in mem[d]:
      mem[n].add(i + n - p - d + 1)
  mem[n].add(1)
  for i in mem[n]:
    if i in k:
      k.remove(i)
      used.add(n)

print(sum(used))
