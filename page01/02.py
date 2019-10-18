def fib():
  a = 1
  b = 2
  while True:
    yield a
    a += b
    yield b
    b += a
ans = 0
for i in filter(lambda x: x%2 == 0, fib()):
  if i > 4000000:
    break
  ans += i
print(ans)
