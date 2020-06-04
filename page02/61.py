fs = [lambda x:  x * (x + 1) // 2, lambda x: x ** 2, lambda x: x * (3 * x - 1) // 2,
      lambda x: x * (2 * x - 1), lambda x: x * (5 * x - 3) // 2, lambda x: x * (3 * x - 2)]
s = list(map(lambda f:
             list(map(lambda x: [x[0], str(x[1])], filter(lambda x: 10000 > x[1] >= 1000,
                         map(lambda x: [x, f(x)], range(150))))), fs))
def fun(nl, value, index):
  if not nl:
    for i, v in s[0]:
      fun(list(range(1, 6)), value + [v], index + [i])
    return
  for n in nl:
    for i, v in s[n]:
      if i not in index and value[-1][2:] == v[:2]:
        if len(index) == 5:
          if v[2:] == value[0][:2]:
            print(sum(map(int, value + [v])))
          return
        tmp = nl.copy()
        tmp.remove(n)
        fun(tmp, value + [v], index + [i])

fun(None, [], [])
