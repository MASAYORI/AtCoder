import itertools


def main():
    n, k = map(int, input().split())
    time = []
    for i in range(n):
        t = list(map(int, input().split()))
        time.append(t)

    ans = 0
    for root in itertools.permutations(range(1, n)):
        now_time = 0
        now_time += time[0][root[0]]
        now_city = root[0]

        for i in range(1, n-1):
            to_city = root[i]
            now_time += time[now_city][to_city]
            now_city = to_city

        now_time += time[now_city][0]

        if now_time == k:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()