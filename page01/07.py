from prime import Prime

p = Prime.prime()
for i in range(10000):
  next(p)

print(next(p))
