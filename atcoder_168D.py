n, m = map(int, input().split())
connect = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False] * (n+1)
visited[1] = True

from collections import deque
que = deque()
que.append(1)
ans = [0]*(n+1)

while len(que)>0:
    now_room = que.popleft()
    for to_room in connect[now_room]:
        if visited[to_room] == False:
            visited[to_room] = True
            ans[to_room] = now_room
            que.append(to_room)

print('Yes')
for i in range(2, n+1):
    print(ans[i])
