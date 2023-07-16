def main():
    while True:
        A, B = map(int, input().split())
        if A == B == 0:
            break
        N = A - B
        if N < 2:
            print(0, 0)
        elif N % 2:
            print((N - 3) // 2, 1)
        else:
            print(N // 2, 0)
        # print(0, 0) if N < 2 else (print((N - 3) // 2, 1) if N % 2 else print(N // 2, 0))


if __name__ == "__main__":
    main()
