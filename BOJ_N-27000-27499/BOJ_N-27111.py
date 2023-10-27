def main():
    N = int(input())

    log = [0] * 200_001
    a, cnt = 0, 0
    for _ in range(N):
        ai, bi = map(int, input().split())
        a = max(a, ai)
        if bi == 0:
            if log[ai] == 1:
                log[ai] = 0
            else:
                cnt += 1
        else:
            if log[ai] == 1:
                cnt += 1
            else:
                log[ai] = 1

    cnt += log[:a+1].count(1)
    print(cnt)


if __name__ == "__main__":
    main()
