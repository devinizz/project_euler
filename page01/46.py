from prime import Prime

for c in range(3, 9999999999999999999999999999999999999999999, 2):
  if Prime.isPrime(c):
    continue
  for i in map(lambda x: x ** 2 * 2, range(1, 1000000000000000000000000000000000000000000)):
    if c < i:
      print(c)
      exit(0)
    if Prime.isPrime(c - i):
      break
