coins = [1, 2, 5, 10, 20, 50, 100, 200]
g = [0] * 201
g[200] = 1
for c in coins:
  for i, j in enumerate(g):
    while i - c >= 0:
      i -= c
      g[i] += j

print(g[0])  
