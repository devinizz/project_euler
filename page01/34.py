from math import factorial
a = list(map(lambda x: factorial(x), range(10)))
ans = 0
for i in range(10, factorial(9) * 7):
  orig = i
  s = 0
  while i > 0:
    s += a[i%10]
    i //= 10
  if orig == s:
    ans += orig

print(ans)
