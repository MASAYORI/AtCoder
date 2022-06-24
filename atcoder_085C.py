n, y = map(int, input().split())
for i in reversed(range(n+1)):
    for j in reversed(range(n+1-i)):
        k = n-i-j
        if y == 10000*i + 5000*j + 1000*k:
            print(i, j, k)
            exit()

print(-1, -1, -1)