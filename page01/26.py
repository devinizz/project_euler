ans = 0
curr = 0
for n in range(1, 1000):
  n_copy = n
  while n % 2 == 0:
    n //= 2
  while n % 5 == 0:
    n //= 5
  for i, j in enumerate(map(lambda x: 10 ** x - 1, range(1, 1000)), start = 1):
    if j % n == 0:
      if i > curr:
        ans = n_copy
        curr = i
      break

print(ans)
