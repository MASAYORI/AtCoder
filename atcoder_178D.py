s = int(input())
dp = [1]*(s+10000)
dp[0] = 0
dp[1] = 0
dp[2] = 0
for i in range(3, s+1):
    for j in range(3, s+1):
        if i+j <= s:
            dp[i+j] += dp[i]
            dp[i+j] %= (10**9 + 7)
print(dp[s] % (10**9 + 7))