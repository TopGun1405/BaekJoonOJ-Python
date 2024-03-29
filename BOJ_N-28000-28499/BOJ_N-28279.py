from collections import deque


def main():
    N = int(input())
    queue = deque()
    for _ in range(N):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            queue.appendleft(cmd[1])

        elif cmd[0] == 2:
            queue.append(cmd[1])

        elif cmd[0] == 3:
            print(queue.popleft() if queue else -1)

        elif cmd[0] == 4:
            print(queue.pop() if queue else -1)

        elif cmd[0] == 5:
            print(len(queue))

        elif cmd[0] == 6:
            print(1 if not queue else 0)

        elif cmd[0] == 7:
            print(queue[0] if queue else -1)

        elif cmd[0] == 8:
            print(queue[-1] if queue else -1)


if __name__ == "__main__":
    main()
