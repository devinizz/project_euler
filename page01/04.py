ans = 0
for i in range(100,1000):
  for j in range(i,1000):
    k = i * j
    a = list(str(k))
    if a == list(reversed(a)):
      ans = max(k, ans)

print(ans)


