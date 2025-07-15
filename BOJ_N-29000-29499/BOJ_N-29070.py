from math import ceil


def main():
    a, b, h, w = map(int, input().split())

    print(ceil(h / a) * ceil(w / b))


if __name__ == "__main__":
    main()
