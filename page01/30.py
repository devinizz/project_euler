p = list(map(lambda x: x ** 5, range(10)))
ans = 0
for i in range(10, p[9] * 6):
  tmp = i
  s = 0
  while i > 0:
    s += p[i%10]
    i //= 10
  if tmp == s:
    ans += tmp

print(ans)
