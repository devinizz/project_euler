from bisect import bisect

class Prime:
  p = [2, 3]
  def isPrime(x):
    p = Prime.p
    while p[-1] < x:
      Prime.next()
    return True if p[bisect(p, x) - 1] == x else False
      
  def next():
    p = Prime.p
    n = p[-1] + 2
    while True:
      for i in p:
        if n % i == 0:
          break
        if i ** 2 > n:
          p.append(n)
          return n
      n += 2

  def prime():
    p = Prime.p
    index = 0
    while True:
      if len(p) > index:
        yield p[index]
        index += 1
      else:
        yield Prime.next()
        index += 1
