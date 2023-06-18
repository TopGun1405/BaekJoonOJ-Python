from collections import deque


def main():
    M, N, H = map(int, input().split())
    tomatoBox = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]

    startHeightRowCol = []
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoBox[h][r][c] == 1:
                    visited[h][r][c] = True
                    startHeightRowCol.append((h, r, c))
    days = changingTomato(tomatoBox, visited, startHeightRowCol)

    for h in range(H):
        for r in tomatoBox[h]:
            if 0 in r:
                print(-1)
                return
    else:
        print(days)


def changingTomato(box: list, visited: list, start: list):
    x = [-1, 1, 0, 0, 0, 0]
    y = [0, 0, -1, 1, 0, 0]
    z = [0, 0, 0, 0, -1, 1]

    queue = deque(start)
    daysQueue = deque([0] * len(queue))

    days = 0
    while queue:
        currH, currR, currC = queue.popleft()
        days = daysQueue.popleft()

        for i in range(6):
            h = currH + z[i]
            r = currR + x[i]
            c = currC + y[i]
            if 0 <= h < len(box) and 0 <= r < len(box[0]) and 0 <= c < len(box[0][0]):
                if not visited[h][r][c]:
                    if box[h][r][c] == 0:
                        box[h][r][c] = 1
                        visited[h][r][c] = True
                        queue.append((h, r, c))
                        daysQueue.append(days + 1)

    return days


if __name__ == "__main__":
    main()
