from prime import Prime
ans = 0
curr = 0
for b in Prime.prime():
  if b > 1000:
    break
  for a in range(-999, 1000):
    n = 0
    for i in map(lambda x: b + a * x + x ** 2, range(2000)):
      if not Prime.isPrime(i):
        break
      n += 1
    if n > curr:
      curr = n
      ans = a * b

print(ans)




