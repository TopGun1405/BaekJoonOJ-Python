def main():
    N = int(input())

    if N == 1:
        print(0)
    else:
        print((N * N) // 2 + (1 if N % 2 == 1 else 0))


if __name__ == "__main__":
    main()
