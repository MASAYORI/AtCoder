
n = int(input())

t_0 = 0
x_0 = 0
y_0 = 0

enable_flag = True
for i in range(n):
    t, x, y = map(int, input().split())
    dt = abs(t - t_0)
    dx = abs(x - x_0)
    dy = abs(y - y_0)

    t_0 = t
    x_0 = x
    y_0 = y

    if (dx + dy > dt) or (dt%2 != (dx + dy)%2):
        enable_flag = False

if enable_flag == False:
    print('No')
else:
    print('Yes')