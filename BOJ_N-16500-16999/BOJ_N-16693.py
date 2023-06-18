import math


def main():
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    print("Slice of pizza" if P1 / A1 < P2 / (math.pi * R1 ** 2)
          else "Whole pizza")


if __name__ == "__main__":
    main()
