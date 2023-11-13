from collections import deque


def main():
    N = int(input())
    array = [deque(map(int, input().split())) for _ in range(N)]

    Q = int(input())
    for _ in range(Q):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            i = cmd[1] - 1
            array[i].appendleft(array[i].pop())

        elif cmd[0] == 2:
            tmp = [deque() for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    tmp[j].appendleft(array[i].popleft())
            array = tmp

    for row in array:
        print(*row)


if __name__ == "__main__":
    main()
