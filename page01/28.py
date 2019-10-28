ans = 1
curr = 1
for i in map(lambda x: x * 2, range(1, 501)):
  for n in range(4):
    curr += i
    ans += curr

print(ans)
