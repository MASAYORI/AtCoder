import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

a_minus = []
for i in range(n):
    a_minus.append((-1)*a[i])

heapq.heapify(a_minus)
for i in range(m):
    x = heapq.heappop(a_minus)
    x /= 2
    x = int(x)
    heapq.heappush(a_minus, x)

ans = (-1)*sum(a_minus)
print(ans)