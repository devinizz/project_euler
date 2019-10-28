def isValid(x, y, z):
  s = [x, y, z]
  a = [0] * 10
  for i in s:
    while i > 0:
      a[i%10] += 1
      i //= 10
  return a[0] == 0 and len(list(filter(lambda x: x == 1, a))) == 9

ans = 0
for i in range(1000, 10000):
  for j in range(1, 100):
    if i % j == 0 and isValid(i, j, i // j):
      ans += i
      break

print(ans)
