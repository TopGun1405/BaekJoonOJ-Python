def main():
    N, D, K = map(int, input().split())
    s = list(map(int, input().split()))

    m = min(map(lambda e: K // e, s))
    c = (D + m - 1) // m

    print(c - 1)


if __name__ == "__main__":
    main()
