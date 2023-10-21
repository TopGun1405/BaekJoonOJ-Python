def main():
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    while True:
        R, C = map(int, input().split())
        if R == C == 0:
            break
        area = [list(input()) for _ in range(R)]
        for x in range(R):
            bomb = []
            for y in range(C):
                if area[x][y] == '*':
                    bomb.append('*')
                else:
                    cnt = 0
                    for i in range(8):
                        r = x + dx[i]
                        c = y + dy[i]
                        if 0 <= r < R and 0 <= c < C:
                            if area[r][c] == '*':
                                cnt += 1
                    bomb.append(cnt)
            print(*bomb, sep='')


if __name__ == "__main__":
    main()
