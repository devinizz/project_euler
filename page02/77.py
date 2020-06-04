from prime import Prime

dp = [0]
for i in range(1, 999999999999999999999):
  dp.append([0] * (i + 1))
  last_p = 0
  for p in Prime.prime():
    if p >= i:
      break
    dp[i][p] = dp[i][last_p] + dp[i-p][min(i - p, p)]
    last_p = p
  if (dp[i][last_p]) > 5000:
    print(i)
    break
  dp[i][i] = dp[i][last_p]
  if p == i:
    dp[i][p] += 1
