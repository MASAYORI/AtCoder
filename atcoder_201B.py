
def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = map(str, input().split())
        t = int(t)
        mountains.append([t, s])
    mountains.sort(key=lambda x: x[0])
    print(mountains[-2][1])



if __name__ == '__main__':
    main()
