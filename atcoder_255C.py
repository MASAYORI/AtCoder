
def main():
    X, A, D, N = map(int, input().split())
    B = A + (N-1)*D
    if D < 0:
        A, B = B, A
        D = abs(D)

    if D == 0:
        ans = abs(X - A)

    elif X <= A:
        ans = A - X
    elif B <= X:
        ans = X - B
    else:
        y = (X - A) % D
        ans = min(y, D - y)

    print(ans)


if __name__ == '__main__':
    main()