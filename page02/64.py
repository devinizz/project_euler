def fun(x):
  bias = int(x ** 0.5) * -1
  if x == bias ** 2:
    return 0
  denominator = 1
  for count in range(1, 9999999999999999999999999999):
    denominator = (x - bias ** 2) / denominator
    tmp = int((x ** 0.5 - bias) / denominator)
    bias = 0 - bias - tmp * denominator
    if denominator == 1:
      return count

print(len(list(filter(lambda x: x & 1 == 1, map(fun, range(10001))))))
