def main():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))

    ans = 0
    for gyou in range(1 << h):
        for retsu in range(1 << w):
            black = 0
            for shift_gyou in range(h):
                for shift_retsu in range(w):
                    if gyou >> shift_gyou & 1 == 0 \
                            and retsu >> shift_retsu & 1 == 0:
                        if c[shift_gyou][shift_retsu] == "#":
                            black += 1
            if black == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
