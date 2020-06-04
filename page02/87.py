from prime import Prime

target = int(5e7)
mask = [1] * target
ans = 0

for i in map(lambda x: x ** 2, Prime.prime()):
  if i >= target:
    break
  for j in map(lambda x: x ** 3, Prime.prime()):
    if i + j >= target:
      break
    for k in map(lambda x: x ** 4, Prime.prime()):
      s = i + j + k
      if s >= target:
        break
      ans += mask[s]
      mask[s] = 0

print(ans)
