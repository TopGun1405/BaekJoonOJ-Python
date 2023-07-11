def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 3:
        print(1 if A[0] * A[1] == A[2] else 0)
    else:
        cnt = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if A[i] * A[j] == A[k]:
                        cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
