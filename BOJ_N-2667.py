from collections import deque


def main():
    N = int(input())
    townMap = [list(map(int, input().strip())) for _ in range(N)]
    house = []
    visited = [[False] * N for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for row in range(N):
        for col in range(N):
            if not visited[row][col] and townMap[row][col]:
                queue = deque([(row, col)])
                visited[row][col] = True
                house.append(1)
                while queue:
                    currR, currC = queue.popleft()
                    for i in range(4):
                        r = currR + dx[i]
                        c = currC + dy[i]
                        if 0 <= r < N and 0 <= c < N:
                            if not visited[r][c] and townMap[r][c]:
                                house[-1] += 1
                                queue.append((r, c))
                                visited[r][c] = True

    print(len(house))
    print(*sorted(house), sep='\n')


if __name__ == "__main__":
    main()
