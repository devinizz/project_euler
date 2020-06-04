from itertools import combinations
numbers = list(map(lambda x: x ** 2, range(1, 10)))
pairs = list(map(lambda n: list(map(lambda x: 6 if x == 9 else x, [n // 10, n % 10])), numbers))

c = list(combinations(list(range(9)) + [6], 6))
ans = 0
for i in c:
  for j in c:
    for a, b in pairs:
      if not ((a in i and b in j) or (b in i and a in j)):
        break
    else:
      ans += 1

print(ans // 2)
