from fractions import Fraction

def f():
  n = Fraction(1)
  while True:
    n = 1 + 1 / (n + 1)
    yield n

ans = 0
for i, j in enumerate(f()):
  if i == 1000:
    break
  if len(str(j.numerator)) > len(str(j.denominator)):
    ans += 1

print(ans)
