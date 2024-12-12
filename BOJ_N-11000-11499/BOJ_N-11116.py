from collections import deque


def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        box_l = deque(map(int, input().split()))
        box_r = deque(map(int, input().split()))

        cars, cnt = 0, 0
        while box_l:
            left = box_l.popleft()
            if left + 1000 in box_r:
                cnt += 1
            if cnt == 2:
                cnt = 0
                cars += 1

        print(cars)


if __name__ == "__main__":
    main()
