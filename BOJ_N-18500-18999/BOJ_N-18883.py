def main():
    N, M = map(int, input().split())
    num = list(range(1, N * M + 1))
    i = 0
    for _ in range(N):
        for j in range(M):
            if j < M - 1:
                print(num[i], end=' ')
            else:
                print(num[i])
            i += 1


if __name__ == "__main__":
    main()
