from collections import deque


def main():
    N, M = map(int, input().split())
    mMap = [list(input()) for _ in range(N)]
    print(findExit(mMap, N - 1, M - 1))


def findExit(mMap, n, m):
    visited = [[False] * len(mMap[0]) for _ in range(len(mMap))]
    x, y = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque([(0, 0)])
    minQueue = deque([1])

    visited[0][0] = True

    while queue:
        currR, currC = queue.popleft()
        length = minQueue.popleft()

        for i in range(len(x)):
            row = currR + x[i]
            col = currC + y[i]

            if 0 <= row < len(mMap) and 0 <= col < len(mMap[0]):
                if not visited[row][col]:
                    if row == n and col == m:
                        return length + 1

                    elif mMap[row][col] == '1':
                        visited[row][col] = True
                        queue.append((row, col))
                        minQueue.append(length + 1)
    return -1


if __name__ == "__main__":
    main()
