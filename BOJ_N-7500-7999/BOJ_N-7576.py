from collections import deque


def main():
    M, N = map(int, input().split())
    tomatoBox = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    startRowCol = []
    for r in range(N):
        for c in range(M):
            if tomatoBox[r][c] == 1:
                visited[r][c] = True
                startRowCol.append((r, c))
    days = changingTomato(tomatoBox, visited, startRowCol)

    for r in range(N):
        if 0 in tomatoBox[r]:
            print(-1)
            break
    else:
        print(days)


def changingTomato(box: list, visited: list, start: list):
    x, y = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque(start)
    daysQueue = deque([0] * len(queue))

    days = 0
    while queue:
        currR, currC = queue.popleft()
        days = daysQueue.popleft()

        for i in range(4):
            r = currR + x[i]
            c = currC + y[i]
            if 0 <= r < len(box) and 0 <= c < len(box[0]):
                if not visited[r][c]:
                    if box[r][c] == 0:
                        box[r][c] = 1
                        visited[r][c] = True
                        queue.append((r, c))
                        daysQueue.append(days + 1)

    return days


if __name__ == "__main__":
    main()
