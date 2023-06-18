def main():
    A = int(input(), 2)
    B = int(input(), 2)
    k = 100_000
    mask = 2 ** k - 1
    ans = list(map(lambda n: bin(n)[2:].zfill(k), [A & B, A | B, A ^ B, mask - A, mask - B]))
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
