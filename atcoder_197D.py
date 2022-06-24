import math

n = int(input())
x_0, y_0 = map(int, input().split())
x_diagonal, y_diagonal = map(int, input().split())
x_center = (x_0 + x_diagonal)/2
y_center = (y_0 + y_diagonal)/2

r = math.sqrt((x_0 - x_diagonal)**2 + (y_0 - y_diagonal)**2)/2
rad = math.radians(360/n)

x_tmp = x_0 - x_center
y_tmp = y_0 - y_center

x_prime = x_tmp*math.cos(rad) - y_tmp*math.sin(rad)
y_prime = x_tmp*math.sin(rad) + y_tmp*math.cos(rad)

x_ans = x_prime + x_center
y_ans = y_prime + y_center

print(x_ans, y_ans)