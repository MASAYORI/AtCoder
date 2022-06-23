
def main():
    a, b, x = map(int, input().split())
    left = 1
    right = 10**20
    price = a*left + b*len(str(left))

    if x < price:
        print(0)
        exit()
    while right - left > 1:
        center = (left + right) // 2
        price = a*center + b*len(str(center))
        if price <= x:
            left = center

        else:
            right = center

    if left > 10**9:
        left = 10**9
    print(left)


if __name__ == '__main__':
    main()
