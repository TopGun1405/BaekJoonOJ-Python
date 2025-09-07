def main():
    N = int(input())
    air = sorted([int(input()) for _ in range(N)])

    p = air[0] - air[-1]//2
    print(p if p > 0 else 0)


if __name__ == "__main__":
    main()
