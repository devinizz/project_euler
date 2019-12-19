from prime import Prime

ans = 1
for p in Prime.prime():
  if ans * p > 1000000:
    break
  ans *= p

print(ans)
