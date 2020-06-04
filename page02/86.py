total = 0

for a in range(9999999999999999):
  for b in range(2, 2 * a + 1):
    c = int((a ** 2 + b ** 2) ** 0.5)
    if a ** 2 + b ** 2 == c ** 2:
      total += b // 2
      total -= max(b - a - 1, 0)
  if total > 1000000:
    print(a)
    break
      
    
