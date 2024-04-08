from collections import deque


def main():
    def breakWall(r: int, c: int, d: int) -> int:
        queue = deque([[r, c, d]])
        visited[r][c][d] = 1

        while queue:
            currR, currC, des = queue.popleft()

            if currR == N - 1 and currC == M - 1:
                return visited[currR][currC][des]

            for i in range(4):
                R = currR + dx[i]
                C = currC + dy[i]
                if N <= R or R < 0 or M <= C or C < 0:
                    continue
                if matMap[R][C] == "1" and des == 0:
                    visited[R][C][1] = visited[currR][currC][des] + 1
                    queue.append([R, C, 1])
                elif matMap[R][C] == "0" and visited[R][C][des] == 0:
                    visited[R][C][des] = visited[currR][currC][des] + 1
                    queue.append([R, C, des])

        return -1

    N, M = map(int, input().split())
    matMap = [list(input()) for _ in range(N)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    print(breakWall(0, 0, 0))


if __name__ == "__main__":
    main()
