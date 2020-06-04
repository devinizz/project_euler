class Prime:
  def __init__(self, n):
    p = []
    b = [True] * n
    b[0] = b[1] = False
    for i in range(2, n):
      if b[i]:
        p.append(i)
      for j in p:
        if i * j >= n:
          break
        b[i*j] = False
        if i % j == 0:
          break
    self.b = b
    self.n = n
    self.p = p

  def isPrime(self, x):
    assert(x <= self.n)
    return self.b[x]

  def getList(self):
    return self.p
