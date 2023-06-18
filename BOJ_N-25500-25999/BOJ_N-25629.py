import math


def main():
    N = int(input())
    a = list(map(int, input().split()))
    x, y = 0, 0
    for i in range(N):
        if a[i] % 2:
            x += 1
        else:
            y += 1
    print(1 if x == math.ceil(N / 2) and y == N // 2 else 0)


if __name__ == "__main__":
    main()
