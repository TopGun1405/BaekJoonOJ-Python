def main():
    while True:
        C, W, L, P = map(int, input().split())
        if C == W == L == P == 0:
            break
        print(1 if C == 1 else C ** (W * L * P))


if __name__ == "__main__":
    main()
