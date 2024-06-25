def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(N)]

    UD = N * M * 2
    LR = 0
    for i in range(N):
        for j in range(M):
            if j == 0:
                LR += S[i][j]
            elif S[i][j-1] < S[i][j]:
                LR += S[i][j] - S[i][j-1]
    LR *= 2
    FB = 0
    for j in range(M):
        for i in range(N):
            if i == 0:
                FB += S[i][j]
            elif S[i-1][j] < S[i][j]:
                FB += S[i][j] - S[i-1][j]
    FB *= 2

    print(UD + LR + FB)


if __name__ == "__main__":
    main()
