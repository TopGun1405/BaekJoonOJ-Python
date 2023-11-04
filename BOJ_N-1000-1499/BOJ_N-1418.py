def main():
    def sieve_of_eratosthenes(num: int) -> list:
        sieve = [True] * (num + 1)
        for i in range(2, int(num ** 0.5) + 1):
            if sieve[i]:
                for j in range(2 * i, num + 1, i):
                    sieve[j] = False
        return sieve

    N = int(input())
    K = int(input())

    prime_list = sieve_of_eratosthenes(N)
    k = [1] * (N + 1)
    for i in range(2, N + 1):
        if prime_list[i] and i > K:
            for j in range(i, N + 1, i):
                k[j] = 0
    print(sum(k) - 1)


if __name__ == "__main__":
    main()
