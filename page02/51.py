from prime import Prime

m = dict()
ans = 0

def Add(s, t, i, n):
  global m
  global ans
  if len(s) == 0:
    return
  c = t + 'x' + s[1:]
  if i == -1 or int(s[0]) == i:
    if c not in m:
      m[c] = list()
    m[c].append(n)
    if len(m[c]) == 8:
      ans = m[c][0] if ans == 0 else min(ans, m[c][0])
    Add(s[1:], t + 'x', int(s[0]), n)
  Add(s[1:], t + s[0], i, n)

i = 0
j = 1
while ans == 0:
  i = j
  j *= 10
  for k in range(i, j):
    if Prime.isPrime(k):
      Add(str(k), '', -1, k)

print(ans)
