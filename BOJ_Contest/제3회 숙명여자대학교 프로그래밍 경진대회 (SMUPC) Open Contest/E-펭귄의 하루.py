from collections import deque


def main():

    def BFS(end: str) -> list:
        fin = []
        visited = [[False] * M for _ in range(N)]
        visited[queue[0][0]][queue[0][1]] = True

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        while queue:
            currR, currC, currTime = queue.popleft()

            for i in range(4):
                R = currR + dx[i]
                C = currC + dy[i]

                if 0 <= R < N and 0 <= C < M:
                    if not visited[R][C]:
                        if town[R][C] == end:
                            visited[R][C] = True
                            fin.append([R, C, currTime + 1])
                            queue.append([R, C, currTime + 1])

                        elif town[R][C] != 'D':
                            visited[R][C] = True
                            queue.append([R, C, currTime + 1])

        return fin if fin else [-1, -1, -1]

    N, M = map(int, input().split())
    town = [list(input()) for _ in range(N)]

    queue = deque()
    for r in range(N):
        for c in range(M):
            if town[r][c] == 'S':
                queue.append([r, c, 0])
                break
        else:
            continue
    res = sorted(BFS('F'), key=lambda k: k[2])[0]

    print(res)
    if res[2] != -1:
        queue = deque([res])
        res = BFS('H')

    print(res[0][2])


if __name__ == "__main__":
    main()
