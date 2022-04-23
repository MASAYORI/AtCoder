def g2(x):
    x = list(str(x))
    x.sort()
    x = int(''.join(x))
    return x


def g1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = int(''.join(x))
    return x


def f(x):
    return g1(x) - g2(x)


def main():
    n, k = map(int, input().split())
    a = n
    for i in range(k):
        a = f(a)
    print(a)


if __name__ == '__main__':
    main()
