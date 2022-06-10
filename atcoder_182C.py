def main():
    n = list(map(int, list(input())))

    def remainder3(i):
        return i % 3

    n_rem = map(remainder3, n)
    n_rem = [i for i in n_rem if i % 3 != 0]

    if sum(n) % 3 == 0:
        print(0)

    if sum(n) % 3 == 1:
        if 1 in n_rem:
            if len(n) > 1:
                print(1)
            else:
                print(-1)
        elif len(n) > 2:
            print(2)
        else:
            print(-1)

    if sum(n) % 3 == 2:
        if 2 in n_rem:
            if len(n) > 1:
                print(1)
            else:
                print(-1)

        elif len(n) > 2:
            print(2)
            exit()

        else:
            print(-1)
            exit()


if __name__ == '__main__':
    main()