f = open('82.txt', 'r')
mat = list(map(lambda x: list(map(int, x.split(','))),
            filter(lambda x: len(x) != 0, f.read().split('\n'))))

for j in range(1, len(mat[0])):
  for i in range(len(mat) - 1):
    mat[i+1][j-1] = min(mat[i+1][j-1], mat[i][j-1] + mat[i][j])
  for i in range(len(mat) - 1, 0, -1):
    mat[i-1][j-1] = min(mat[i-1][j-1], mat[i][j-1] + mat[i][j])
  for i in range(len(mat)):
    mat[i][j] += mat[i][j-1]

print(min(map(lambda x: x[-1], mat)))
