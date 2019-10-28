from prime import Prime

def isPrime(x):
  for i in Prime.prime():
    if i ** 2 > x:
      return True
    if x % i == 0:
      return False

ans = 0
def f(x, n):
  if n == 10:
    return
  for i in range(n):
    r = x % (10 ** i)
    a = (x - r) * 10 + r + n * (10 ** i)
    if isPrime(a):
      global ans
      ans = max(ans, a)
    f(a, n + 1)

f(1, 2)
print(ans)
