def main():
    def sieve_of_eratosthenes(n: int) -> list:
        sieve = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(2 * i, n, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    N = int(input())
    prime_list = sieve_of_eratosthenes(10_000)
    for n1, n2 in zip(prime_list[:-1], prime_list[1:]):
        if n1 * n2 > N:
            print(n1 * n2)
            break


if __name__ == "__main__":
    main()
