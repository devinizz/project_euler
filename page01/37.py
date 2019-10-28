from prime import Prime
left = {2, 3, 5, 7}
right = {2, 3, 5, 7}
ans = 0
count = 0
while len(left) != 0 and len(right) != 0 and count < 11:
  l = set()
  r = set()
  for i in left:
    for j in range(1, 10):
      n = int(str(j) + str(i))
      if Prime.isPrime(n):
        l.add(n)
  for i in right:
    for j in range(1, 10):
      n = i * 10 + j
      if Prime.isPrime(n):
        r.add(n)
  left = l
  right = r
  for i in left.intersection(right):
    ans += i
    count += 1

print(ans)
