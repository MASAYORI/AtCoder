mod = 998244353


def main():
    N, M, K = map(int, input().split())
    dp = [[0]*(K+1) for i in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j >= k:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod

    print(sum(dp[N]) % mod)


if __name__ == '__main__':
    main()
