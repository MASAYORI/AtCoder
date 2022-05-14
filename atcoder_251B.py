
def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    st = set()
    for i in range(N):
        if A[i] <= W:
            st.add(A[i])
        for j in range(i+1, N):
            if A[i] + A[j] <= W:
                st.add(A[i]+A[j])
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] <= W:
                    st.add(A[i] + A[j] + A[k])
    print(len(st))




if __name__ == '__main__':
    main()
