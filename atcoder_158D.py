from collections import deque


def main():
    s = list(input())
    q = int(input())
    inv_flag = False

    s_deque = deque()
    for i in range(len(s)):
        s_deque.append(s[i])

    for i in range(q):
        query = list(input().split())
        if query[0] == '1':
            if not inv_flag:
                inv_flag = True
            else:
                inv_flag = False

        else:
            if query[1] == '1':
                if not inv_flag:
                    s_deque.appendleft(query[2])
                else:
                    s_deque.append(query[2])
            if query[1] == '2':
                if not inv_flag:
                    s_deque.append(query[2])
                else:
                    s_deque.appendleft(query[2])

    if inv_flag:
        s_deque.reverse()

    print(*s_deque, sep='')


if __name__ == '__main__':
    main()