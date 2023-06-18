from collections import deque


def main():
    N = int(input())
    Deque = deque()
    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "push_front":
            Deque.appendleft(int(cmd[1]))
        elif cmd[0] == "push_back":
            Deque.append(int(cmd[1]))
        elif cmd[0] == "pop_front":
            print(Deque.popleft() if len(Deque) > 0 else -1)
        elif cmd[0] == "pop_back":
            print(Deque.pop() if len(Deque) > 0 else -1)
        elif cmd[0] == "size":
            print(len(Deque))
        elif cmd[0] == "empty":
            print(1 if len(Deque) == 0 else 0)
        elif cmd[0] == "front":
            print(Deque[0] if len(Deque) > 0 else -1)
        elif cmd[0] == "back":
            print(Deque[-1] if len(Deque) > 0 else -1)


if __name__ == "__main__":
    main()
