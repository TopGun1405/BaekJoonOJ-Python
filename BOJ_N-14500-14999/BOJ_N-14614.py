def main():
    A, B, C = map(int, input().split())

    res = A
    for _ in range(C % 2):
        res ^= B

    print(res)


if __name__ == "__main__":
    main()
