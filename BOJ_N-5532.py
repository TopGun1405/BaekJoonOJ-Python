import math


def main():
    L = int(input())
    A, B = int(input()), int(input())
    C, D = int(input()), int(input())
    print(L - math.ceil(A / C) if math.ceil(A / C) >= math.ceil(B / D)
          else L - math.ceil(B / D))


if __name__ == "__main__":
    main()
