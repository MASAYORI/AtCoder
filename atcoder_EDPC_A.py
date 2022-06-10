
def main():
    n = int(input())
    h = [0] + list(map(int, input().split()))
    dp = [10**15]*(n+1)
    dp[1] = 0
    dp[2] = abs(h[2] - h[1])
    for i in range(3, n+1):
        cost1 = dp[i-1] + abs(h[i-1] - h[i])
        cost2 = dp[i-2] + abs(h[i-2] - h[i])
        dp[i] = min(cost1, cost2)
print(dp[n])


if __name__ == '__main__':
    main()
