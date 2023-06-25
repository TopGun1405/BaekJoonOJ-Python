from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        box = [list(input()) for _ in range(3)]
        display = list(map(int, input().split()))
        n, a = display.pop(0), display

        queue = deque()
        connected = []
        visited = [[False] * 3 for _ in range(3)]
        dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
        for i in range(3):
            for j in range(3):
                if box[i][j] == 'O' and not visited[i][j]:
                    visited[i][j] = True
                    queue.append((i, j))
                    connected.append(1)

                while queue:
                    R, C = queue.popleft()
                    for n in range(4):
                        r, c = R + dx[n], C + dy[n]
                        if 0 <= r < 3 and 0 <= c < 3:
                            if box[r][c] == 'O' and not visited[r][c]:
                                visited[r][c] = True
                                queue.append((r, c))
                                connected[-1] += 1

        print(1 if a == sorted(connected) else 0)


if __name__ == "__main__":
    main()
