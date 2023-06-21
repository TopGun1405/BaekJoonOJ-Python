def main():
    N, M = map(int, input().split())
    rect = [list(input()) for _ in range(N)]
    i, j, d = -1, -1, 0
    for r in range(N):
        for c in range(M):
            if rect[r][c] == '#':
                if i == j == -1:
                    i, j = r, c
                d = max(d, rect[r].count('#'))

    iMid, jMid = i + d // 2, j + d // 2
    if rect[i][jMid] == '.':
        print("UP")
    elif rect[i + d - 1][jMid] == '.':
        print("DOWN")
    elif rect[iMid][j] == '.':
        print("LEFT")
    else:
        print("RIGHT")


if __name__ == "__main__":
    main()
