dp = [1] + [0] * 100
for i in range(1, len(dp) - 1):
  for j in range(i, len(dp)):
    dp[j] = dp[j] + dp[j-i]

print(dp[100])
