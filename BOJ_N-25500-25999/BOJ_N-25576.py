def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    K = [list(map(int, input().split())) for _ in range(N-1)]

    cnt = 0
    for i in range(N-1):
        tot = 0
        for j in range(M):
            tot += abs(L[j] - K[i][j])
        if tot > 2_000:
            cnt += 1

    print("YES" if cnt >= (N - 1) / 2 else "NO")


if __name__ == "__main__":
    main()
