from itertools import *

op = [lambda x, y: x + y, lambda x, y: x - y,
      lambda x, y: x * y, lambda x, y: x / y if y != 0 else 0]

def count(n):
  s = set()
  for d1, d2, d3, d4 in permutations(n):
    for o1, o2, o3 in product(op, repeat = 3):
      for r in [o3(o2(o1(d1, d2), d3), d4), o2(o1(d1, d2), o3(d3, d4))]:
        if r == int(r):
          s.add(int(r))
  return next(filter(lambda x: x not in s, range(1, 999999)))

ans = max(combinations(range(10), 4), key = count)
print(''.join(map(str, ans)))
