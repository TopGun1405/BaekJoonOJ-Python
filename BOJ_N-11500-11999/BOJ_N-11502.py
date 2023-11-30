def main():
    T = int(input())

    sieve = [True] * 1_001
    for i in range(2, int(1_001 ** 0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(2*i, 1_001, i):
            sieve[j] = False

    for _ in range(T):
        K = int(input()) - 3
        for i in range(2, 1_001):
            if sieve[i] and sieve[K-i]:
                print(*sorted([i, K-i, 3]))
                break


if __name__ == "__main__":
    main()
