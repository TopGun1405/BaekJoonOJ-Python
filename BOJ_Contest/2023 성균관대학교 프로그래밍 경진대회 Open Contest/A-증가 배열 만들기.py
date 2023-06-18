from collections import deque


def main():
    N, M, K = map(int, input().split())
    A = [[1] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx, dy = [1, 0], [0, 1]

    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()
        for i in range(2):
            row = r + dx[i]
            col = c + dy[i]
            if 0 <= row < N and 0 <= col < M:
                if not visited[row][col]:
                    visited[row][col] = True
                    A[row][col] = A[r][c] + 1
                    queue.append((row, col))

    if A[N-1][M-1] > K:
        print("NO")
    else:
        print("YES")
        for a in A:
            print(*a)


if __name__ == "__main__":
    main()
