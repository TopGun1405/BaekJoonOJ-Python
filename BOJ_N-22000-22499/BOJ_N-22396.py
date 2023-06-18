def main():
    while True:
        R0, W0, C, R = map(int, input().split())
        if R0 == W0 == C == R == 0:
            break
        k = (W0 * C - R0) // R
        p = (W0 * C - R0) % R
        print([(k + 1, k)[p == 0], 0][k < 0])


if __name__ == "__main__":
    main()
