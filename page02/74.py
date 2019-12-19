from math import factorial
r = [0] * 9000000

def fun(n):
  def g(n, L):
    if r[n] != 0:
      return r[n]
    s = sum(map(lambda x: factorial(int(x)), str(n)))
    if r[s] != 0:
      pass
    elif s in L:
      index = L.index(s)
      for i in L[index:]:
        r[i] = len(L) - index
    else:
      g(s, L + [s])
    if r[n] == 0:
      r[n] = r[s] + 1
    return r[n]

  return g(n, [n])

print(len(list(filter(lambda x: x == 60, map(lambda x: fun(x), range(1000000))))))
