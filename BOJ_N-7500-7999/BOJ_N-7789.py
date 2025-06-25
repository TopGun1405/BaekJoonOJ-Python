def main():
    def check_prime():
        for i in range(2, int(N ** 0.5) + 1):
            if not sieve[i]:
                continue
            for j in range(2 * i, N + 1, i):
                sieve[j] = False

    tel, n = input().split()

    N = 10 ** 7
    sieve = [True] * (N + 1)

    check_prime()

    print("Yes" if sieve[int(tel)] and sieve[int(n + tel)] else "No")


if __name__ == "__main__":
    main()
