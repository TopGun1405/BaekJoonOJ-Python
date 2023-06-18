def main():
    while True:
        B, N = map(int, input().split())
        if B == N == 0:
            break
        n = int(B ** (1 / N))
        print(n if abs(B - n ** N) < abs(B - (n + 1) ** N) else n + 1)


if __name__ == "__main__":
    main()
