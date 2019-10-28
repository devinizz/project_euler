s = set()
for a in range(2, 101):
  curr = a
  for b in range(99):
    curr *= a
    s.add(curr)

print(len(s))
