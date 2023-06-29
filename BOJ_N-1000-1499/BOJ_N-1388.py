from collections import deque


def main():
    N, M = map(int, input().split())
    floor = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    board = 0
    for R in range(N):
        for C in range(M):

            if not visited[R][C]:
                queue = deque([(R, C)])

                while queue:
                    r, c = queue.popleft()
                    visited[r][c] = True
                    if floor[r][c] == '-':
                        if c + 1 < M and floor[r][c + 1] == '-':
                            queue.append((r, c + 1))

                    elif floor[r][c] == '|':
                        if r + 1 < N and floor[r + 1][c] == '|':
                            queue.append((r + 1, c))
                board += 1

    print(board)


if __name__ == "__main__":
    main()
