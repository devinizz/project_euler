def to(n):
  return "".join(sorted(str(n)))

c = dict()
for i in map(lambda x: x ** 3, range(99999999999999999999999999999999999)):
  s = to(i)
  c[s] = c.get(s, [])
  c[s].append(i)
  if len(c[s]) == 5:
    print(min(c[s]))
    break

