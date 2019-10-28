def get(x):
  s = [0] * 10
  s[0] = 1
  count = 0
  r = 0
  for i in range(1, 100):
    if count == 9:
      return r
    t = str(i * x)
    for d in map(lambda c: int(c), t):
      if s[d] == 1:
        return 0
      s[d] = 1
      count += 1
      r = r * 10 + d

ans = 0
for i in range(9999):
  ans = max(get(i), ans)

print(ans)
