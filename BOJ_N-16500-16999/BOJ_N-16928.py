from collections import deque


def main():
    N, M = map(int, input().split())

    ladders = {}
    for _ in range(N):
        x, y = map(int, input().split())
        ladders[x] = y

    snakes = {}
    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    queue = deque([1])
    board = [0] * 101
    visited = [False, True] + [False] * 99
    while queue:
        currPos = queue.popleft()
        for num in [1, 2, 3, 4, 5, 6]:
            pos = currPos + num
            if 0 < pos <= 100 and not visited[pos]:
                if ladders.get(pos, 0):
                    pos = ladders[pos]

                if snakes.get(pos, 0):
                    pos = snakes[pos]

                if not visited[pos]:
                    queue.append(pos)
                    visited[pos] = True
                    board[pos] = board[currPos] + 1

    print(board[100])


if __name__ == "__main__":
    main()
