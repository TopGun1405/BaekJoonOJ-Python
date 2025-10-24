from math import ceil


def main():
    C = int(input())

    n = ceil(C ** 0.5) + 2

    print("x" * n)
    for _ in range(n-2):
        print("x" + "."*(n-2) + "x")
    print("x" * n)


if __name__ == "__main__":
    main()
