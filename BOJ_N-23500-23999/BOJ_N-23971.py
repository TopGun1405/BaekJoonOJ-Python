import math


def main():
    H, W, N, M = map(int, input().split())
    print(math.ceil(H / (N + 1)) * math.ceil(W / (M + 1)))


if __name__ == "__main__":
    main()
