bound = int(1e9)
ans = 0

for n in range(1, int((bound / 4) ** 0.5)):
  nn = n ** 2
  for mm in (3 * nn + 1, 3 * nn - 1):
    m = mm ** 0.5
    if m.is_integer():
      for perimeter in (4 * mm, 18 * nn + 2 * mm + 12 * int(m) * n):
        ans += perimeter if perimeter < bound else 0

print(ans)
