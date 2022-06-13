def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_ex = []

    for i in range(n):
        p_ex.append((1 + p[i])/2)

    p_ex_Cum = [p_ex[0]]
    for i in range(1, n):
        p_ex_Cum.append(p_ex_Cum[i-1] + p_ex[i])

    ans = -10**15
    for i in range(n-k+1):
        if i == 0:
            ans_tmp = p_ex_Cum[i+k-1]
        else:
            ans_tmp = p_ex_Cum[i+k-1] - p_ex_Cum[i-1]

        ans = max(ans, ans_tmp)

    print(ans)


if __name__ == '__main__':
    main()