def main():
    N = int(input())
    area = [list(input()) for _ in range(N)]

    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    for x in range(N):
        bomb = []
        for y in range(N):
            if area[x][y] != '.':
                bomb.append('*')
            else:
                cnt = 0
                for i in range(8):
                    r = x + dx[i]
                    c = y + dy[i]
                    if 0 <= r < N and 0 <= c < N:
                        if area[r][c] != '.':
                            cnt += int(area[r][c])
                bomb.append(cnt if cnt < 10 else 'M')
        print(*bomb, sep='')


if __name__ == "__main__":
    main()
