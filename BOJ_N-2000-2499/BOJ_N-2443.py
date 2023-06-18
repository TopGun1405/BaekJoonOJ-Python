def main():
    N = int(input())
    for i in range(N):
        print(" " * i + "*" * (2 * N - (2 * i + 1)))


if __name__ == "__main__":
    main()
