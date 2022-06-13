def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_a = list(map(int, input().split()))
        c.append(c_a[0])
        a.append(c_a[1:])

    ans = 10**15
    for i in range(1<<n):
        cost = 0
        skill = [0]*m

        for shift in range(n):
            if i>>shift & 1 == 1:
                cost += c[shift]
                for j in range(m):
                    skill[j] += a[shift][j]

        if x <= min(skill):
            ans = min(ans, cost)

    if ans == 10**15:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()