from prime import Prime

def t():
  n = 1
  r = 0
  while True:
    r += n
    yield r
    n += 1

for n in t():
  count = 1
  curr = n
  for p in Prime.prime():
    c = 1
    while n % p == 0:
      c += 1
      n //= p
    count *= c
    if n == 1:
      break
  if count > 500:
    print(curr)
    break

