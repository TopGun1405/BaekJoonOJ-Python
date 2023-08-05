def main():
    N = int(input())
    res = [1, 2] * (N // 2) + ([3] if N % 2 else [])
    print(*res)


if __name__ == "__main__":
    main()
