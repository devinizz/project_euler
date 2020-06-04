from functools import reduce
import itertools

f = open('79.txt', 'r')
keys = list(set(filter(lambda x: len(x) != 0, f.read().split('\n'))))
digits = dict.fromkeys('0123456789', 0)
for k in keys:
  for d in digits:
    digits[d] = max(digits[d], k.count(d))

base = reduce(lambda x, d: x + [d] * digits[d], digits, [])
used = reduce(lambda x, d: x + [d] * min(digits[d], 1), digits, [])

def gen():
  for i in range(999999999):
    for j in itertools.combinations_with_replacement(used, i):
      yield list(j)

def valid(pwd):
  for key in keys:
    if reduce(lambda index, x: pwd.find(x, index), key, 0) == -1:
      return False
  return True

for i in gen():
  for j in itertools.permutations(base + i):
    s = ''.join(j)
    if valid(s):
        print(s)
        exit(0)
