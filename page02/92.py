from math import factorial
from functools import reduce
from itertools import combinations_with_replacement
from collections import Counter

flag = [0] * (9 ** 2 * 7 + 1)
flag[0] = 1
flag[1] = 1
flag[89] = 89

def square_sum(n):
  return sum(map(lambda x: int(x) ** 2, n))

def get(n):
  if flag[n] == 0:
    flag[n] = get(square_sum(str(n)))
  return flag[n]

ans = 0
for i in combinations_with_replacement(range(10), 7):
  if get(square_sum(i)) == 89:
    ans += factorial(7) // reduce(lambda x, y: x * factorial(y), Counter(i).values(), 1)

print(ans)
