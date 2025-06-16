def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    cnt = 0
    for _ in range(N-1):
        K_i = list(map(int, input().split()))
        tot = 0
        for j in range(M):
            tot += abs(L[j] - K_i[j])
        if tot > 2_000:
            cnt += 1

    print("YES" if cnt >= (N - 1) / 2 else "NO")


if __name__ == "__main__":
    main()
