available = range(32, 127)
def fun(b, n, c, a):
  if len(b) == 0:
    return [c, a]
  for i in range(3):
    t = b[i] ^ n[i]
    if t not in available:
      return [0, 0]
    a += t
    if t == ord(' '):
      c += 1
  return fun(b[3:], n, c, a) 

f = open('59.txt', 'r')
b = list(map(lambda x: int(x), f.read().split(',')))
p = [[i, j, k]
     for i in range(ord('a'), ord('z') + 1)
     for j in range(ord('a'), ord('z') + 1)
     for k in range(ord('a'), ord('z') + 1)]
print(max(map(lambda n: fun(b, n, 0, 0), p))[1])
