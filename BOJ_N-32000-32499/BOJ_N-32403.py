def main():
    N, T = map(int, input().split())
    a = list(map(int, input().split()))

    n = []
    for i in range(1, int(T ** 0.5) + 1):
        if T % i == 0:
            n.append(i)
            if T / i != i:
                n.append(T // i)

    cnt = 0
    for a_i in a:
        minCnt = 1_001
        for n_i in n:
            minCnt = min(minCnt, abs(a_i - n_i))
        cnt += minCnt

    print(cnt)


if __name__ == "__main__":
    main()
