def sqrt_100_sum(x):
  y = int(x ** 0.5)
  x -= y ** 2
  if x == 0:
    return 0
  while y < 10 ** 99:
    x *= 100
    y *= 10
    q = x // (2 * y)
    if q * (2 * y + q) > x:
      q -= 1
    x -= q * (2 * y + q)
    y += q
  return sum(map(int, str(y)))

print(sum(map(sqrt_100_sum, range(1, 101))))
