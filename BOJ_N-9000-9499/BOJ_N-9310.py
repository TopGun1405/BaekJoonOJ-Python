def main():
    while True:
        N = int(input())
        if N == 0:
            break
        a1, a2, a3 = map(int, input().split())
        if a2 - a1 == a3 - a2:
            d = a2 - a1
            print((N * (2 * a1 + (N - 1) * d)) // 2)
        elif a2 / a1 == a3 / a2:
            r = a2 // a1
            print(a1 * (r ** N - 1) // (r - 1))


if __name__ == "__main__":
    main()
