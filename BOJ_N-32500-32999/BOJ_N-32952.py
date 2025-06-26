def main():
    R, K, M = map(int, input().split())

    i = M // K
    while i > 0 and R > 0:
        R //= 2
        i -= 1

    print(R)


if __name__ == "__main__":
    main()
