f = open('81.txt', 'r')
mat = list(map(lambda x: list(map(int, x.split(','))),
            filter(lambda x: len(x) != 0, f.read().split('\n'))))
for i in range(1, len(mat[0])):
  mat[0][i] += mat[0][i-1]

for i in range(1, len(mat)):
  mat[i][0] += mat[i-1][0]
  for j in range(1, len(mat[0])):
    mat[i][j] += min(mat[i-1][j], mat[i][j-1])

print(mat[-1][-1])
