from math import gcd
def isValid(x, y):
  s = [x, y]
  a = []
  b = []
  while x > 0:
    a.append(x % 10)
    x //= 10
  while y > 0:
    if y % 10 in a:
      a.remove(y % 10)
    else:
      b.append(y % 10)
    y //= 10
  return len(a) == 1 and s[0] * b[0] == s[1] * a[0]

n = 1
d = 1
for i in filter(lambda x: x % 10 != 0, range(10, 100)):
  for j in range(11, i):
    if isValid(i, j):
      n *= j
      d *= i

print(d // gcd(n, d))
