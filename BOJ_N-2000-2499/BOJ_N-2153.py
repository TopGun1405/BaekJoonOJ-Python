def main():
    N = 52 * 20
    sieve = [True] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(2 * i, N + 1, i):
            sieve[j] = False

    word = input()
    n = 0
    for c in word:
        n += int(ord(c) - (96 if ord(c) >= 97 else 38))

    print(f"It is{' ' if sieve[n] else ' not '}a prime word.")


if __name__ == "__main__":
    main()
