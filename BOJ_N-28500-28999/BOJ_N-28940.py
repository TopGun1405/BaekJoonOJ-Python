from math import ceil


def main():
    w, h = map(int, input().split())
    n, a, b = map(int, input().split())
    print(-1 if w < a or h < b else ceil(n / ((w // a) * (h // b))))


if __name__ == "__main__":
    main()
