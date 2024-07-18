def main():
    n, m = map(int, input().split())
    board = [input().split() for _ in range(n)]

    r, c = 0, 0
    max9 = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            cnt += board[i][j].count("9")
        if cnt > max9:
            r, max9 = i, cnt

    for j in range(m):
        cnt = 0
        for i in range(n):
            cnt += board[i][j].count("9")
        if cnt > max9:
            r, c, max9 = 0, j, cnt

    cntHit = 0
    for i in range(n):
        if r == i and r != -1:
            continue
        for j in range(m):
            if c == j and c != -1:
                continue
            cntHit += board[i][j].count("9")

    print(cntHit)


if __name__ == "__main__":
    main()
