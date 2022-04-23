
def main():
    n = int(input())
    ans = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            ans.append(i)
            if n // i != i:
                ans.append(n // i)
        i += 1
    ans.sort()
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
