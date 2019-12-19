ans = 0
for i in range(9999999999999999999999999999):
  if 9 ** (i + 1) < 10 ** i:
    print(ans)
    break
  for n in range(9, 0, -1):
    if n ** (i + 1) < 10 ** i:
      break
    ans += 1 
