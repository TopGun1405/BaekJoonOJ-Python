import math


def main():
    N, A, B, C, D = map(int, input().split())
    print(math.ceil(N / A) * B if math.ceil(N / A) * B < math.ceil(N / C) * D
          else math.ceil(N / C) * D)


if __name__ == "__main__":
    main()
