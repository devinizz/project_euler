abundant = []
s = set()
ans = 1
for n in range(2, 28124):
  if n not in s:
    ans += n
  t = 1
  for i in range(2, 200):
    if i * i > n:
      break
    if n % i == 0:
      t += i
      if i * i != n:
        t += n // i
  if t > n:
    abundant.append(n)
    for i in abundant:
      s.add(n + i)

print(ans)
