def fun(s):
  n = 10 + sum(s[:2])
  r = []
  for i in map(lambda x: [n - sum(x)] + x, map(lambda x: (s + [s[0]])[x:x+2], range(5))):
    r += i
  return r

ans = max(map(lambda x: min(map(lambda n: x[n:] + x[:n], range(0, 15, 3))), 
        filter(lambda x: set(x) == set(range(1,11)),
          map(fun, filter(lambda x: 0 not in x and sum(x) % 5 == 0 and len(set(x)) == 5,
            map(lambda x: list(map(int, list(str(x)))), range(10000, 99999)))))))
for i in ans:
  print(i, end='')
print("")
