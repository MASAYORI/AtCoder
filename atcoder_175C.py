def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        ans = x - k*d
    else:
        ans = x - d*(x // d) -d*((k - x//d)%2)
    print(abs(ans))


if __name__ == '__main__':
    main()