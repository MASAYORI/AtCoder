
def main():
    n = int(input())
    n_init = n

    i = 2
    ans = 0
    while i*i <= n_init:
        if n == 1:
            break
        count = 0
        tmp = 0
        while n % i == 0:
            n = n // i
            tmp += 1
            if count < tmp:
                count = tmp
                tmp = 0
                ans += 1

        i += 1

    if n != 1:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
