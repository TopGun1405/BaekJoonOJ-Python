def main():
    N = int(input())

    if N >= 1_000_000:
        M = int(N * 0.2)
    elif N >= 500_000:
        M = int(N * 0.15)
    elif N >= 100_000:
        M = int(N * 0.1)
    else:
        M = int(N * 0.05)

    print(M, N-M)


if __name__ == "__main__":
    main()
