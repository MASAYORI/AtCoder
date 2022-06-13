def main():
    a, b, w = map(int, input().split())
    w = 1000*w
    max_ans = -10**15
    min_ans = 10**15

    for x in range(10**6 + 10):
        if a*x <= w <= b*x:
            max_ans = max(max_ans, x)
            min_ans = min(min_ans, x)

    if min_ans == 10**15:
        print('UNSATISFIABLE')
    else:
        print(min_ans, max_ans)


if __name__ == '__main__':
    main()