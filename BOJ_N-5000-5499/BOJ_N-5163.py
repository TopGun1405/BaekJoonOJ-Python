from math import pi


def main():
    K = int(input())
    for x in range(1, K+1):
        b, w = map(float, input().split())
        V = 0
        for _ in range(int(b)):
            r = float(input())
            V += (4 / 3) * pi * r**3
        V /= 1000

        print(f"Data Set {x}:")
        print("Yes" if V >= w else "No")
        if x < K:
            print()


if __name__ == "__main__":
    main()
