from prime import Prime

curr = 0
for n in range(2, 999999999999999999999999999999999999999999999999999):
  if curr == 4:
    print(n - 4)
    break
  count = 0
  for p in Prime.prime():
    if n % p == 0:
      count += 1
      while n % p == 0:
        n //= p
    if Prime.isPrime(n):
      count += 1
      break
    if n == 1:
      break
  if count == 4:
    curr += 1
  else:
    curr = 0
