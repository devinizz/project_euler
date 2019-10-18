f = open('22.txt')
name = f.read()
name = list(map(lambda x: x.strip('"'), name.split(',')))
name.sort()
ans = 0
for i in range(len(name)):
  s = sum(map(lambda x: ord(x) - 64, name[i]))
  ans += (i + 1) * s

print(ans)
