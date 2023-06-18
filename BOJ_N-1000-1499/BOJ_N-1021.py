from collections import deque


def main():
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))
    queue = deque([n for n in range(1, N + 1)])

    rotateCnt = 0
    for pos in positions:
        while queue[0] != pos:
            if queue.index(pos) <= len(queue) // 2:
                queue.rotate(-1)
            else:
                queue.rotate(1)
            rotateCnt += 1
        else:
            queue.popleft()
    print(rotateCnt)


if __name__ == "__main__":
    main()
