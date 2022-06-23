
def main():
    h_w = list(map(int, input().split()))
    ans = 0

    for a in range(1, 31):
        for b in range(1, 31):
            for d in range(1, 31):
                for e in range(1, 31):
                    c = h_w[0] - a -b
                    f = h_w[1] - d - e
                    g = h_w[3] - a - d
                    h = h_w[4] - b - e
                    i1 = h_w[2] - g - h
                    i2 = h_w[5] - c - f

                    if min(c, f, g, h, i1, i2) > 0 and i1==i2:
                        ans += 1
    print(ans)






if __name__ == '__main__':
    main()
