from collections import deque


def is_7_in(n):
    # n_list = list(map(int, str(n))) こっちならint型のリスト
    n_list = str(n)
    if "7" in n_list:
        return True
    else:
        return False


def decimal_to_octal(x):
    numbers = deque()
    while x >= 8:
        numbers.appendleft(x%8)
        x //= 8
    numbers.appendleft(x)
    return int(''.join([str(n) for n in numbers]))


def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if not is_7_in(decimal_to_octal(i)):
            if not is_7_in(i):
                ans += 1
    print(ans)






if __name__ == '__main__':
    main()
