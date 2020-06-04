def f(x):
  return x * (x + 1) // 2

target = int(2*10**6)
curr = 0
ans = 0
for i in range(1, 999999999999):
  a = f(i)
  for j in range(1, i + 1):
    b = f(j)
    if abs(curr - target) > abs(a * b - target):
      curr = a * b
      ans = i * j
    if a * b > target:
      break
  if a > target:
    break

print(ans)
