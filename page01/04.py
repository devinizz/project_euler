ans = 0
for i in range(100,1000):
  for j in range(i,1000):
    k = i * j
    a = []
    while k > 0:
      a.append(k % 10)
      k //= 10
    if a == list(reversed(a)):
      ans = max(i * j, ans) 

print(ans)


