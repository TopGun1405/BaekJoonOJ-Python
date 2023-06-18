def main():
    N, M = map(int, input().split())
    castle = [input() for _ in range(N)]

    r, c = 0, 0
    for i in range(N):
        r = r + (0 if 'X' in castle[i] else 1)

    for i in range(M):
        c = c + (0 if 'X' in [castle[j][i] for j in range(N)] else 1)
    print(max(r, c))


if __name__ == "__main__":
    main()
