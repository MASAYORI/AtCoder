def main():

    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    visited = [-1]*(n+1)
    visited[1] = 0
    now_town = 1
    move_count = 0
    for i in range(k+10):
        move_count += 1
        now_town = a[now_town]
        if move_count == k:
            print(now_town)
            exit()
        if visited[now_town] == -1:
            visited[now_town] = move_count
        else:
            cycle = move_count - visited[now_town]
            break
        
    k -= move_count
    k %= cycle
    for i in range(k):
        now_town = a[now_town]
    print(now_town)

if __name__ == '__main__':
    main()
