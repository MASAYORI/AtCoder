
def main():
    n = int(input())
    target = n*2
    x = 1
    ans = 0
    while x*x < 2*n:
        if target % x == 0:
            y = target // x
            if x%2 != y%2:
                ans += 2
        x += 1

    print(ans)


if __name__ == '__main__':
    main()
