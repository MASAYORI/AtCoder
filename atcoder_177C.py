def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A) - A[n-1]
    ans = 0
    for i in reversed(range(1, n)):
        ans += A_sum*A[i]
        A_sum -= A[i-1]

    print(ans % (10**9 + 7))


if __name__ == '__main__':
    main()