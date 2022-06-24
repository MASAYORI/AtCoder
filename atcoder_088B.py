from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()
que = deque(a)
alice = 0
bob = 0
for i in range(n):
    if i%2 == 0:
        alice += que.pop()
    if i%2 == 1:
        bob += que.pop()
print(alice - bob)

