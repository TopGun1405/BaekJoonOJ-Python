def main():
    while True:
        N = int(input())
        if N == 0:
            break
        a, b, c = map(int, input().split())
        if b - a == c - b:
            d = b - a
            print((N * (2 * a + (N - 1) * d)) // 2)
        elif b / a == c / b:
            r = b // a
            print(a * (r ** N - 1) // (r - 1))


if __name__ == "__main__":
    main()
