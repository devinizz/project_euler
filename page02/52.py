def fun(n):
  return sorted(str(n))

for i in range(1, 9999999999999999999999999999):
  if fun(i) == fun(2*i) == fun(3*i) == fun(4*i) == fun(5*i) == fun(6*i):
    print(i)
    break
