from collections import deque


def main():
    N, K = map(int, input().split())
    positionQueue = deque([N])
    movement = [lambda k: 2 * k, lambda k: k - 1, lambda k: k + 1]
    takeTime = [lambda t: t, lambda t: t + 1, lambda t: t + 1]
    times = [1e9] * 100_001

    times[N] = 0
    while positionQueue:
        currP = positionQueue.popleft()
        for i in range(3):
            p = movement[i](currP)
            if 0 <= p <= 100_000:
                check = [times[p] > times[currP],
                         times[p] > times[currP] + 1,
                         times[p] > times[currP] + 1]
                if check[i]:
                    positionQueue.append(p)
                    times[p] = takeTime[i](times[currP])

    print(times[K])


if __name__ == "__main__":
    main()
