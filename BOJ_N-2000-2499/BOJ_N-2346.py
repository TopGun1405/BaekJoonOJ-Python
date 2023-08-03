from collections import deque


def main():
    N = int(input())
    balloons = deque(enumerate(map(int, input().split())))
    popNum = []
    while True:
        idx, n = balloons.popleft()
        popNum.append(idx + 1)

        if not balloons:
            break

        for _ in range(abs(n) + (0 if n < 0 else -1)):
            if n > 0:
                balloons.append(balloons.popleft())
            else:
                balloons.appendleft(balloons.pop())
    print(*popNum)


if __name__ == "__main__":
    main()
