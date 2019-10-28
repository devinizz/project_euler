from math import sqrt
s = [0] * 1001
for i in range(1, 400):
  for j in range(i, 1000 - 2 * i):
    k = i ** 2 + j ** 2
    k = sqrt(k)
    r = i + j + int(k)
    if r > 1000:
      break
    if int(k) == k:
      s[r] += 1

ans = 0
curr = 0
for i, j in reversed(list(enumerate(s))):
  if j == 0:
    continue
  t = i
  while True:
    if s[t] > curr:
      curr = s[t]
      ans = t
    t += i
    if t > 1000:
      break
    s[t] += j 

print(ans)
