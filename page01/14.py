s=dict()
s[1] = 1
def f(n):
  global s
  if s.get(n) == None:
    if n % 2 == 0:
      s[n] = f(n // 2) + 1
    else:
      s[n] = f(n * 3 + 1) + 1
  return s[n]

curr = 1
ans = 1
for i in range(1, 1000000):
  if f(i) > curr:
    curr = f(i)
    ans = i

print(ans)
      
