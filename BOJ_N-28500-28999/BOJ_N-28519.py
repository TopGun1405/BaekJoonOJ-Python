def main():
    n, m = map(int, input().split())
    print(2 * min(n, m) + 1 if n != m else 2 * n)


if __name__ == "__main__":
    main()
