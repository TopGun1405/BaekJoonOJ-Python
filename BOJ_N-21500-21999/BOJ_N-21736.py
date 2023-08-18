from collections import deque


def main():
    N, M = map(int, input().split())
    campus = [input() for _ in range(N)]

    queue = deque([])
    visited = [[False for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I' and not visited[r][c]:
                queue.append([r, c])
                visited[r][c] = True
                break
        else:
            continue

    met = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                if campus[x][y] == 'P':
                    met += 1
                if campus[x][y] != 'X':
                    queue.append([x, y])
                    visited[x][y] = True

    print(met if met else "TT")


if __name__ == "__main__":
    main()
