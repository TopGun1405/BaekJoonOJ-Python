def main():
    N = int(input())
    for i in range(1, N + 1):
        print("*" * i)
    for i in range(1, N):
        print("*" * (N - i))


if __name__ == "__main__":
    main()
