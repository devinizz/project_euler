ans = 0
for i in range(1000000):
  tmp = i
  b10 = 0
  b2 = 0
  while i > 0:
    b10 = b10 * 10 + i % 10
    i //= 10
  i = tmp
  while i > 0:
    b2 = b2 * 2 + i % 2
    i //= 2
  if tmp == b2 == b10:
    ans += tmp

print(ans)
