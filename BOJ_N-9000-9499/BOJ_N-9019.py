from collections import deque


def main():
    T = int(input())
    commands = {
        'D': lambda n: 2 * int(n) % 10_000,
        'S': lambda n: (n - 1) % 10_000,
        'L': lambda n: n // 1_000 + (n % 1_000) * 10,
        'R': lambda n: n // 10 + (n % 10) * 1000
    }
    for _ in range(T):
        A, B = map(int, input().split())

        queue = deque([A])
        cmdQueue = deque([''])
        visited = [False] * 10_001

        visited[A] = True
        while queue:
            num = queue.popleft()
            currCmd = cmdQueue.popleft()

            if num == B:
                print(currCmd)
                break

            for cmd, operation in commands.items():
                k = operation(num)
                if not visited[k]:
                    visited[k] = True
                    queue.append(k)
                    cmdQueue.append(currCmd + cmd)


if __name__ == "__main__":
    main()
