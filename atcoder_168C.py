
def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        a, b = map(int, input().split())
        friends.append([a, b])
    friends.sort()

    ans = K
    for friend in friends:
        if friend[0] <= ans:
            ans += friend[1]
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
