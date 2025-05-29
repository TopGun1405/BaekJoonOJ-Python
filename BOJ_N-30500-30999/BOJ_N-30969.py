def main():
    N = int(input())

    jinju, cnt = 0, 0
    cost = {n: 0 for n in range(1, 1_001)}
    for _ in range(N):
        D_i, C_i = input().split()
        C_i = int(C_i)

        if D_i == "jinju":
            jinju = C_i

        if C_i > 1_000:
            cnt += 1
        else:
            cost[C_i] += 1

    for n in range(jinju+1, 1_001):
        cnt += cost[n]

    print(jinju)
    print(cnt)


if __name__ == "__main__":
    main()
