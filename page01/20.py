from math import factorial

n = factorial(100)
ans = 0
while n > 0:
  ans += n % 10
  n //= 10

print(ans)
