from math import factorial
a = list(range(10))
left = 999999
ans = 0
while len(a) > 0:
  n = left // factorial(len(a) - 1)
  left %= factorial(len(a) - 1)
  n = a.pop(n)
  ans = ans * 10 + n

print(ans)

