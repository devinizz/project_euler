from prime import Prime
ans = 0
for i in range(2, 1000000):
  r = str(i)
  while i > 0:
    if not Prime.isPrime(int(r)):
      break
    r = str(i%10) + r[:-1]
    i //= 10
  if i == 0:
    ans += 1

print(ans)
