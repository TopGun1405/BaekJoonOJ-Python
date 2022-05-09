def main():
    N, T, C, P = map(int, input().split())
    print((N - 1) // T * C * P)


if __name__ == "__main__":
    main()
