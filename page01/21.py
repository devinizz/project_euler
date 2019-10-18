d = [0, 0]
ans = 0
for i in range(2, 10000):
  s = 1
  for n in range(2, 101):
    if n * n > i:
      break
    if i % n == 0:
      s += n
      if i != n * n:
        s += i // n
  d.append(s)
  if s < i and d[s] == i:
    ans += s
    ans += i

print(ans)


      

