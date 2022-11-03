import sys


def main():
    N, M, B = map(int, input().split())
    area = []
    for _ in range(N):
        area += list(map(int, input().split()))

    time, groundHeight = sys.maxsize, 0
    for height in range(min(area), max(area) + 1):
        minTime, maxTime = 0, 0

        for i in range(N * M):
            if area[i] >= height:
                maxTime += area[i] - height
            else:
                minTime += height - area[i]
        if maxTime + B >= minTime and minTime + maxTime * 2 <= time:
            time = minTime + maxTime * 2
            groundHeight = height
    print(time, groundHeight)


if __name__ == "__main__":
    main()
