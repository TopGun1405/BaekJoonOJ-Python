from collections import deque


def main():
    A, B = map(int, input().split())
    queue = deque([(A, 1)])
    operation = [lambda n: n * 2, lambda n: 10 * n + 1]

    while queue:
        num, opCnt = queue.popleft()
        if num > B:
            continue
        elif num == B:
            print(opCnt)
            break
        for op in operation:
            queue.append((op(num), opCnt + 1))
    else:
        print(-1)


if __name__ == "__main__":
    main()
