
def main():
    N, X = map(int, input().split())
    drink = 0
    for i in range(N):
        V, P = map(int, input().split())
        drink += V * P
        if drink > X*100:
            print(i+1)
            exit()

    print(-1)


if __name__ == '__main__':
    main()
