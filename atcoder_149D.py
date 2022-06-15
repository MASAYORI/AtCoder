
def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())

    ans = 0
    point = {'p': S, 'r': P, 's': R}
    myhands = {'p': 's', 'r': 'p', 's': 'r'}
    hands = []
    for i in range(N):
        if i < K:
            ans += point[T[i]]
            hands.append(myhands[T[i]])
        elif hands[i-K] != myhands[T[i]]:
            ans += point[T[i]]
            hands.append(myhands[T[i]])
        else:
            hands.append('x')

    print(ans)


if __name__ == '__main__':
    main()
