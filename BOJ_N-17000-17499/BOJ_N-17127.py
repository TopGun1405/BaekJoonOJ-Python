def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    first = 1
    for i in range(N - 3):
        first *= A[i]
        second = 1
        for j in range(i + 1, N - 2):
            second *= A[j]
            third = 1
            for k in range(j + 1, N - 1):
                third *= A[k]
                fourth = 1
                for w in range(k + 1, N):
                    fourth *= A[w]
                P = max(P, first + second + third + fourth)
    print(P)


if __name__ == "__main__":
    main()
