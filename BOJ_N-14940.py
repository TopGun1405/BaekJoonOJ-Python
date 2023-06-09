from collections import deque


def main():
    n, m = map(int, input().split())
    mapinfo = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque([])
    distance = deque([0])
    for r in range(n):
        for c in range(m):
            if mapinfo[r][c] == 2:
                queue.append((r, c))
                visited[r][c] = 0
            elif mapinfo[r][c] == 0:
                visited[r][c] = 0

    while queue:
        currR, currC = queue.popleft()
        currD = distance.popleft()

        for i in range(4):
            r = currR + dx[i]
            c = currC + dy[i]
            if 0 <= r < n and 0 <= c < m:
                if visited[r][c] == -1:
                    if mapinfo[r][c] == 1:
                        visited[r][c] = currD + 1
                        queue.append([r, c])
                        distance.append(currD + 1)

    for r in range(n):
        print(*visited[r])


if __name__ == "__main__":
    main()
