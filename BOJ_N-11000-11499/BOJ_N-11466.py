def main():
    h, w = map(int, input().split())
    m, n = max(h, w), min(h, w)
    print(max((m / 3 if m / 3 <= n else n), n / 2))


if __name__ == "__main__":
    main()
