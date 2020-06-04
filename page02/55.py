bound = 2 ** 51 * 9999

def f(n):
  def rev(n):
    r = 0
    while n > 0:
      r = r * 10 + n % 10
      n //= 10
    return r

  def Lychrel(n):
    if n > bound:
      return True
    r = rev(n)
    if r == n:
      return False
    return Lychrel(r + n)
  
  return Lychrel(n + rev(n))

print(len(list(filter(f, range(10000)))))
