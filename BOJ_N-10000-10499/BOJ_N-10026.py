from collections import deque


def main():
    def RGB(R, C):
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        queue = deque([(R, C)])
        visited[R][C] = True

        while queue:
            currR, currC = queue.popleft()
            for i in range(4):
                x = currR + dx[i]
                y = currC + dy[i]
                if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                    if picture[x][y] == picture[currR][currC]:
                        queue.append((x, y))
                        visited[x][y] = True

    N = int(input())
    picture = [list(input().strip()) for _ in range(N)]
    normal, colorWeakness = 0, 0

    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                RGB(r, c)
                normal += 1

    for r in range(N):
        for c in range(N):
            if picture[r][c] == 'G':
                picture[r][c] = 'R'

    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                RGB(r, c)
                colorWeakness += 1

    print(normal, colorWeakness)


if __name__ == "__main__":
    main()
