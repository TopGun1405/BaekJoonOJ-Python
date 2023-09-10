def main():
    N = input()
    n, lN = 0, len(N)
    for i in range(lN - 1):
        n += (i + 1) * 9 * (10 ** i)
    n += lN * (int(N) - 10 ** (lN - 1) + 1)
    print(n)


if __name__ == "__main__":
    main()
