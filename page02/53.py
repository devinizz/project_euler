ans = 0
for i in range(1, 101):
  n = i
  r = 1
  p = 1
  while n != 0:
    p *= n
    p //= r
    n -= 1
    r += 1
    if p > 1000000:
      ans += 1

print(ans)
