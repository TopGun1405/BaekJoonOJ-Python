from collections import deque


def main():
    T = int(input())
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for _ in range(T):
        M, N, K = map(int, input().split())
        # field = []
        field = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, input().split())
            field[Y][X] = 1

        bug = 0
        for c in range(N):
            for r in range(M):
                if not visited[c][r] and field[c][r] == 1:
                    visited[c][r] = True
                    queue = deque([(r, c)])
                    while queue:
                        currR, currC = queue.popleft()
                        for i in range(4):
                            row = currR + dx[i]
                            col = currC + dy[i]
                            if 0 <= row < M and 0 <= col < N:
                                if not visited[col][row] and field[col][row] == 1:
                                    queue.append((row, col))
                                    visited[col][row] = True
                    bug += 1
        print(bug)


if __name__ == "__main__":
    main()
