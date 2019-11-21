from prime import Prime

def isPrime(n):
  for i in Prime.prime():
    if i ** 2 > n:
      return True
    if n % i == 0:
      return False

def f():
  n = 1
  s = 1
  while True:
    s += 2
    yield [s, list(map(lambda x: n + x * (s - 1), range(1,5)))]
    n += (s - 1) * 4
    
n = 1
d = 0
for s, l in f():
  n += 4 
  d += len(list(filter(lambda x: isPrime(x), l)))
  if n > d * 10:
    print(s)
    break
