def main():
    n = int(input())
    s = list(input())
    q = int(input())
    inv_flag = False
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if not inv_flag:
                s[a-1], s[b-1] = s[b-1], s[a-1]
            else:
                if a <= n:
                    a += n
                else:
                    a -= n

                if b <= n:
                    b += n
                else:
                    b -= n
                s[a - 1], s[b - 1] = s[b - 1], s[a - 1]

        else:
            if inv_flag:
                inv_flag = False
            else:
                inv_flag = True

    if inv_flag:
        ans = s[n:] + s[:n]
    else:
        ans = s[:n] + s[n:]
    print(*ans, sep='')


if __name__ == '__main__':
    main()