f = open('67.txt')
t = f.read()
t = list(map(lambda x: list(map(lambda y: int(y), x.split())),
      filter(lambda x: len(x) != 0, t.split('\n'))))
for i in range(1, len(t)):
  t[i][0] += t[i-1][0]
  t[i][i] += t[i-1][i-1]
  for j in range(1, len(t[i]) - 1):
    t[i][j] += max(t[i-1][j-1], t[i-1][j])

print(max(t[len(t)-1]))
