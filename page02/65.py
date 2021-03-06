from fractions import Fraction

def fun(n):
  if n == 0:
    return 2
  elif n % 3 == 2:
    return (n + 1) * 2 // 3
  else:
    return 1

ans = Fraction(0)
for i in map(fun, reversed(range(100))):
  ans += i
  ans = 1 / ans

print(sum(map(int, str(ans.denominator))))
