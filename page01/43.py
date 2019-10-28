def valid(x):
  s = str(x)
  if int(s[1:4]) % 2 == 0 and \
     int(s[2:5]) % 3 == 0 and \
     int(s[3:6]) % 5 == 0 and \
     int(s[4:7]) % 7 == 0 and \
     int(s[5:8]) % 11 == 0 and \
     int(s[6:9]) % 13 == 0 and \
     int(s[7:10]) % 17 == 0:
    return True
  return False
ans = 0
def f(x, n):
  if n == 10:
    for i in range(9):
      r = x % (10 ** i)
      a = (x - r) * 10 + r
      if valid(a):
        global ans
        ans += a
    return

  for i in range(n):
    r = x % (10 ** i)
    a = (x - r) * 10 + r + n * (10 ** i)
    f(a, n + 1)

f(1, 2)
print(ans)
