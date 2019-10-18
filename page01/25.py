def fib():
  a = 1
  b = 1
  while True:
    yield a
    a += b
    yield b
    b += a

for i, j in enumerate(fib(), start = 1):
  if j >= 10**999:
    print(i)
    break
