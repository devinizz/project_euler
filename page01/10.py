def prime(x):
  p = []
  np = [False] * x
  for n in range(2, x):
    if not np[n]:
      p.append(n)
    for i in p:
      if i * n >= x:
        break
      np[i * n] = True
      if n % i == 0:
        break
  return p

print(sum(prime(2000000)))
