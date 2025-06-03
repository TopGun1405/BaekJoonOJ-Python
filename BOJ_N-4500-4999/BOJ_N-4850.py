def main():
    while True:
        try:
            N, w, d, tot = map(int, input().split())
            totW = N * (N - 1) // 2 * w
            res = abs(tot - totW) // d

            print(N if res == 0 else res)
        except EOFError:
            break


if __name__ == "__main__":
    main()
