from bisect import bisect

class Fun:
  def __init__(self, n):
    self.p = [1]
    self.d = n
    self.n = 1 + self.d
  def isFun(self, x):
    while self.p[-1] < x:
      self.next()
    return True if self.p[bisect(self.p, x) - 1] == x else False
  def next(self):
    self.p.append(self.p[-1] + self.n)
    self.n += self.d
    return self.p[-1]
  def gen(self):
    index = 0
    while True:
      if index >= len(self.p):
        yield self.next()
      else:
        yield self.p[index]
      index += 1


T = Fun(1)
P = Fun(3)
H = Fun(4)
catch = False
for i in H.gen():
  if T.isFun(i) and P.isFun(i):
    if catch:
      print(i)
      break
    if i == 40755:
      catch = True
