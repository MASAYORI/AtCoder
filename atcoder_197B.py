
def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    grid = []
    for i in range(h):
        s = list(input())
        grid.append(s)

    ans = 0
    for i in range(1, h):
        if 0 <= x-i < h:
            if grid[x-i][y] == '#':
                break
            else:
                ans += 1

    for i in range(1, h):
        if 0 <= x+i < h:
            if grid[x+i][y] == '#':
                break
            else:
                ans += 1

    for i in range(1, w):
        if 0 <= y-i < w:
            if grid[x][y-i] == '#':
                break
            else:
                ans += 1

    for i in range(1, w):
        if 0 <= y+i < w:
            if grid[x][y+i] == '#':
                break
            else:
                ans += 1
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
