import random

def isPrime(n, times):
  def miller_test(last, curr, count):
    if curr == 1 and (last == 1 or last == n - 1):
      return True
    if count == 0:
      return False
    return miller_test(curr, pow(curr, 2, n), count - 1)

  d = n - 1
  count = 0
  while d % 2 == 0:
    d //= 2
    count += 1
  for i in range(times):
    r = random.randint(2, n - 1)
    if not miller_test(1, pow(r, d, n), count):
      return False
  return True
