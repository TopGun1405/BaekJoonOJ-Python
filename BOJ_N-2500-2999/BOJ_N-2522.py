def main():
    N = int(input())
    for i in range(1, N + 1):
        print(" " * (N - i) + "*" * i)
    for i in range(1, N):
        print(" " * i + "*" * (N - i))


if __name__ == "__main__":
    main()
