vm = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
for i in range(2, 10):
  vm[str(i)] = i
sm = {'C' : 0, 'D' : 1, 'S' : 2, 'H' : 3}
def fun(x):
  v = [0] * 15
  s = [0] * 4
  for i in x:
    v[vm[i[0]]] += 1
    s[sm[i[1]]] += 1
  r = [0] * 9
  r[8] = max(map(lambda x: x[0] if x[1] != 0 else 0, enumerate(v)))
  r[7] = max(map(lambda x: x[0] if x[1] == 2 else 0, enumerate(v)))
  r[6] = r[7] if len(list(filter(lambda x: x == 2, v))) == 2 else 0
  r[5] = max(map(lambda x: x[0] if x[1] == 3 else 0, enumerate(v)))
  tmp = list(map(lambda x: 1 if x != 0 else 0, v))
  r[4] = max(map(lambda x: x[0] if x[1] == 5 else 0,
                 enumerate(map(lambda x: sum(tmp[x-5:x]), range(5, 15)), start = 1)))
  r[3] = r[8] if len(list(filter(lambda x: x == 5, s))) == 1 else 0
  r[2] = r[5] if r[5] != 0 and r[7] != 0 else 0
  r[1] = max(map(lambda x: x[0] if x[1] == 4 else 0, enumerate(v)))
  r[0] = r[4] if r[4] != 0 and r[3] != 0 else 0
  return r 

f = open('54.txt', 'r')
hand = list(map(lambda x: x.split(), filter(lambda x: len(x) != 0, f.read().split('\n'))))
print(len(list(filter(lambda x: fun(x[:5]) > fun(x[5:]), hand))))
