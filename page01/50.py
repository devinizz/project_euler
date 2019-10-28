from prime import Prime

longest = 0
ans = 0
Prime.isPrime(1000000)
for i in range(0, len(Prime.p)):
  curr = 0
  value = 0
  for j in range(i, len(Prime.p)):
    curr += 1
    value += Prime.p[j]
    if value > 1000000:
      break
    if Prime.isPrime(value) and curr > longest:
      longest = curr
      ans = value
  if longest >= curr:
    break

print(ans)

    


