def main():
    n, m = map(int, input().split())
    print(n // m)
    print(n - m * (n // m))


if __name__ == "__main__":
    main()
