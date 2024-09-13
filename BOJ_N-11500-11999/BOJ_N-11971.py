def main():
    N, M = map(int, input().split())
    limit = []
    for _ in range(N):
        s, v = map(int, input().split())
        for _ in range(s):
            limit.append(v)

    yj = []
    for _ in range(M):
        s, v = map(int, input().split())
        for _ in range(s):
            yj.append(v)

    maxV = 0
    for i in range(100):
        maxV = max(maxV, yj[i] - limit[i])

    print(maxV)


if __name__ == "__main__":
    main()
