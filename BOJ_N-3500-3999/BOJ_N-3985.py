def main():
    L = int(input())
    N = int(input())

    cake = [0] * (L + 1)
    maxReal, maxRealNum = 0, 0
    maxExpect, maxExpectNum = 0, 0
    for n in range(1, N+1):
        P_i, K_i = map(int, input().split())

        if K_i - P_i > maxExpect:
            maxExpect, maxExpectNum = K_i - P_i, n

        cnt = 0
        for i in range(P_i, K_i+1):
            if not cake[i]:
                cnt += 1
                cake[i] = n

        if cnt > maxReal:
            maxReal, maxRealNum = cnt, n

    print(maxExpectNum)
    print(maxRealNum)


if __name__ == "__main__":
    main()
