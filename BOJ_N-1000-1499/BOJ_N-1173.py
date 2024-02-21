def main():
    N, m, M, T, R = map(int, input().split())

    cnt, t, current = 0, 0, m
    while cnt < N:
        if m + T > M:
            break
        if current + T <= M:
            current += T
            cnt += 1
        else:
            current = max(current - R, m)
        t += 1

    print(t if cnt == N else -1)


if __name__ == "__main__":
    main()
