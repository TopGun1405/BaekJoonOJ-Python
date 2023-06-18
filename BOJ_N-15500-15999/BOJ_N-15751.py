def main():
    a, b, x, y = map(int, input().split())
    a, b = min(a, b), max(a, b)
    x, y = min(x, y), max(x, y)
    print(abs(a - x) + abs(b - y))


if __name__ == "__main__":
    main()
