from prime import Prime

def toKey(n):
  return int(''.join(sorted(str(n))))

s = list(map(lambda x: list(), range(10000)))
for i in range(1000,10000):
  if Prime.isPrime(i):
    s[toKey(i)].append(i)

for t in s:
  for i in range(len(t) - 2):
    for j in range(i + 1, len(t) - 1):
      if t[j] * 2 - t[i] in t:
        print(t[i], t[j], t[j] * 2 - t[i])
  
    
