def f():
  n = 1
  while True:
    for i in map(int, str(n)):
      yield i
    n += 1

s = [1, 9, 90, 900, 9000, 90000, 900000]
ans = 1
c = f()
for i in s:
  for j in range(i):
    p = next(c)
  ans *= p

print(ans)
