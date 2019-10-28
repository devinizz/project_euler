from bisect import bisect

f = open('42.txt')
word = f.read()
word = list(map(lambda x: x.strip('"'), word.split(',')))
class Tri:
  t = [1]
  def next():
    t = Tri.t
    t.append(t[-1] + len(t) + 1)
    return t[-1]
  def isTri(x):
    t = Tri.t
    while t[-1] < x:
      Tri.next()
    return True if t[bisect(t, x) - 1] == x else False

ans = 0
for i in word:
  if Tri.isTri(sum(map(lambda c: ord(c) - 64, i))):
    ans += 1

print(ans)
