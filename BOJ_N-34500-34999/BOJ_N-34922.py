from math import pi


def main():
    w, h = map(int, input().split())
    r = int(input())

    print((w * h) - (r**2 * pi)/4)


if __name__ == "__main__":
    main()
