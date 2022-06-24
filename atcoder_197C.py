n = int(input())
a = list(map(int, input().split()))

def calc_or(left, right):
    result = 0
    for i in range(left, right):
        result = result | a[i]

    return result

ans = 2**40
for i in range(1<<(n+1)):
    if i & 1 == 0 or i>>n & 1 == 0:
        continue
    partitions = []
    for shift in range(n+1):
        if i>>shift & 1 == 1:
            partitions.append(shift)
    
    ans_tmp = 0
    for j in range(len(partitions)-1):
        ans_tmp = ans_tmp^calc_or(partitions[j], partitions[j+1])
    ans = min(ans, ans_tmp)

print(ans)
