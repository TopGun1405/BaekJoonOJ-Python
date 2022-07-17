import math


def main():
    R, C, N = map(int, input().split())
    print(int(math.ceil(R / N)) * int(math.ceil(C / N)))


if __name__ == "__main__":
    main()
