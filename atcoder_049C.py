from collections import deque
s = input()

terms = ['dream', 'dreamer', 'erase', 'eraser']
que = deque()
now_t = ''
que.append(now_t)
while(len(que) > 0):
    now_t = que.popleft()
    # print('now_t:', now_t)
    if now_t == s:
        print('YES')
        exit()
    for term in terms:
        tmp_t = now_t + term
        if s.startswith(tmp_t):
            que.append(tmp_t)
print('NO')

