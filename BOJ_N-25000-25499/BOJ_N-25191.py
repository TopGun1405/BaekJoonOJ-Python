def main():
    N = int(input())
    A, B = map(int, input().split())

    print(A // 2 + B if N > A // 2 + B else N)


if __name__ == "__main__":
    main()
