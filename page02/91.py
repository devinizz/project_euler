ans = 0
for x1 in range(51):
  for y1 in range(51) if x1 != 0 else range(1, 51):
    for x2 in range(x1, 51):
      for y2 in range(51) if x1 != x2 else range(y1 + 1, 51):
        x3 = x1 - x2
        y3 = y1 - y2
        if x1 * x2 + y1 * y2 == 0 or \
           x1 * x3 + y1 * y3 == 0 or \
           x2 * x3 + y2 * y3 == 0:
            ans += 1

print(ans)
