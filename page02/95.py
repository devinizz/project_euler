bound = int(1e6)

count = [0] * bound
for i in range(1, bound // 2):
  for j in range(2 * i, bound, i):
    count[j] += i

flag = [0] * bound
def find(n):
  if flag[n] == 0:
    s = set()
    p = n
    while p not in s:
      s.add(p)
      flag[p] = -1
      p = count[p]
      if p > bound:
        return -1
    l = list()
    while p in s:
      l.append(p)
      s.remove(p)
      p = count[p]
    for i in l:
      flag[i] = len(l)
  return flag[n] 

print(max(range(1, bound), key = find))
