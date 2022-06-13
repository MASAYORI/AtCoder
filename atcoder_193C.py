import math


def main():
    N = int(input())
    ans_set = set()
    iter_num = 10**5 + 10
    for a in range(2, iter_num):
        for b in range(2, 34):
            if a**b <= N:
                ans_set.add(a**b)
            else:
                break
    print(N - len(ans_set))


if __name__ == '__main__':
    main()