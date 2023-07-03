def main():
    N, M = map(int, input().split())
    busNum = list(map(int, input().split()))
    cost = [list(map(int, input().split())) for _ in range(N)]

    tot = 0
    for i in range(M - 1):
        tot += cost[busNum[i] - 1][busNum[i + 1] - 1]
    print(tot)


if __name__ == "__main__":
    main()
