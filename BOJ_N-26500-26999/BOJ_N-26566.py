import math


def main():
    n = int(input())
    for _ in range(n):
        A1, P1 = map(int, input().split())
        R1, P2 = map(int, input().split())
        print("Whole pizza" if P1 / A1 > P2 / (R1**2 * math.pi) else "Slice of pizza")


if __name__ == "__main__":
    main()
