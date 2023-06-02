def main():
    N = int(input())
    wire = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda k: k[0])
    wireCnt, maxCnt = [1] * N, 1
    for i in range(1, N):
        for j in range(i):
            if wire[i][1] > wire[j][1]:
                wireCnt[i] = max(wireCnt[i], wireCnt[j] + 1)
                maxCnt = max(maxCnt, wireCnt[i])
    print(N - maxCnt)


if __name__ == "__main__":
    main()
