from collections import deque


def main():

    def melting_cheese():
        queue = deque([[0, 0]])
        visited[0][0] = True

        while queue:
            R, C = queue.popleft()
            for i in range(4):
                row, col = R+dx[i], C+dy[i]
                if 0 <= row < N and 0 <= col < M:
                    if not visited[row][col] and not board[row][col]:
                        queue.append([row, col])
                        visited[row][col] = 1
                    elif board[row][col] == 1:
                        visited[row][col] += 1

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    melting_time = 0
    while True:
        visited = [[0] * M for _ in range(N)]
        melting_cheese()
        melting_time += 1
        for r in range(N):
            for c in range(M):
                if visited[r][c] >= 2:
                    board[r][c] = 0

        air = 0
        for r in range(N):
            for c in range(M):
                if not board[r][c]:
                    air += 1

        if air == N * M:
            break

    print(melting_time)


if __name__ == "__main__":
    main()
