from collections import deque


def main():
    n, m = map(int, input().split())
    connect = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        connect[a].append(b)

    def bfs(start):
        visited = [False] * (n + 1)
        visited[start] = True
        count = 1
        que = deque()
        que.append(start)

        while len(que) > 0:
            now_city = que.popleft()
            for to_city in connect[now_city]:
                if not visited[to_city]:
                    visited[to_city] = True
                    count += 1
                    que.append(to_city)
        return count

    ans = 0
    for i in range(1, n+1):
        ans += bfs(i)

    print(ans)



if __name__ == '__main__':
    main()