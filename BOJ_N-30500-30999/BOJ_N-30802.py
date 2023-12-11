def main():
    N = int(input())
    # S, M, L, XL, XXL, XXXL = map(int, input().split())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())

    t, p = 0, N // P
    for size in sizes:
        if size % T == 0:
            t += size // T
        else:
            t += size // T + 1

    print(t)
    print(p, N - P * p)


if __name__ == "__main__":
    main()
