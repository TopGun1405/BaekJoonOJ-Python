def main():
    N = int(input())
    while N % 2:
        N = N // 2 + 1
    print(N)


if __name__ == "__main__":
    main()
