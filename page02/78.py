from numba import jit

@jit
def solve():
  mod = 10 ** 6
  bound = 10 ** 5
  dp = [0] * bound
  dp[0] = 1
  for i in range(1, bound):
    for j in range(i, bound):
      dp[j] = (dp[j] + dp[j-i]) % mod
    if dp[i] == 0:
      print(i)
      break

solve()
