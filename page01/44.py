from bisect import bisect

class Pen:
  p = [1]
  def isPen(x):
    p = Pen.p
    while p[-1] < x:
      Pen.next()
    return True if p[bisect(p, x) - 1] == x else False
  def next():
    p = Pen.p
    p.append(p[-1] + len(p) * 3 + 1)
    return p[-1]
  def pen(n):
    while n >= len(Pen.p):
      Pen.next()
    return Pen.p[n]

for i in range(10000000000000000000000000000):
  for n in range(1, 1000000000000000000000000000000000000000000000):
    if Pen.pen(i) * 2 % n != 0:
      continue
    r = Pen.pen(i) * 2 // n - 3 * n
    if r < 0:
      break
    if r % 6 == 5 and Pen.isPen(Pen.pen(r // 6) * 2 + Pen.pen(i)):
      print(Pen.pen(i))
      exit(0)
