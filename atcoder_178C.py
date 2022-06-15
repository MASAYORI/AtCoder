def main():
    n = int(input())
    mod = 10**9+7
    all = pow(10, n, mod)
    not_zero = pow(9, n, mod)
    not_nine = pow(9, n, mod)
    not_zero_or_nine = pow(8, n, mod)
    not_zero_and_nine = not_zero + not_nine - not_zero_or_nine
    ans = all - not_zero_and_nine

    print(ans % mod)


if __name__ == '__main__':
    main()
