from fractions import Fraction

# general solution of Pell's equation
def cf(x):
  bias = int(x ** 0.5)
  cf = [bias]
  if x == bias ** 2:
    return [] 
  denominator = 1
  while True:
    denominator = (x - bias ** 2) / denominator
    tmp = int((x ** 0.5 + bias) / denominator)
    cf.append(tmp)
    bias = tmp * denominator - bias
    if denominator == 1:
      if len(cf) % 2 == 0:
        return cf + cf[1:-1]
      return cf[:-1]

def calc(s):
  r = Fraction(0)
  for i in reversed(s):
    r += i
    r = 1 / r
  return r.denominator

print(max(map(lambda x: [calc(cf(x)), x], range(1001)))[1])
