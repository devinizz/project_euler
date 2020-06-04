from heapq import heapify, heappush, heappop
f = open('83.txt', 'r')
mat = list(map(lambda x: list(map(int, x.split(','))),
            filter(lambda x: len(x) != 0, f.read().split('\n'))))

dj = list(map(lambda x: [-1] * len(mat[0]), range(len(mat))))
h = []
heapify(h)
heappush(h, [mat[0][0], 0, 0])

while len(h) != 0:
  x = heappop(h)
  v, i, j = x[0], x[1], x[2]
  if dj[i][j] != -1:
    continue
  dj[i][j] = v
  if i != 0:
    heappush(h, [v + mat[i-1][j], i-1, j])
  if i != len(mat) - 1:
    heappush(h, [v + mat[i+1][j], i+1, j])
  if j != 0:
    heappush(h, [v + mat[i][j-1], i, j-1])
  if j != len(mat[0]) - 1:
    heappush(h, [v + mat[i][j+1], i, j+1])

print(dj[-1][-1])
