from collections import deque


def main():
    R, C = map(int, input().split())
    field = [list(input()) for _ in range(R)]

    queue = deque()
    grassClumps = 0
    visited = [[False] * C for _ in range(R)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(R):
        for j in range(C):
            if field[i][j] == '#' and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                grassClumps += 1

                while queue:
                    r, c = queue.popleft()
                    for n in range(4):
                        dr, dc = r + dx[n], c + dy[n]
                        if 0 <= dr < R and 0 <= dc < C:
                            if field[dr][dc] == '#' and not visited[dr][dc]:
                                visited[dr][dc] = True
                                queue.append((dr, dc))

    print(grassClumps)


if __name__ == "__main__":
    main()
