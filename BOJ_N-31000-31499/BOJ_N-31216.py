def main():
    N = 1_000_000
    sieve = [False, False] + [True] * (N-1)
    for i in range(2, N+1):
        if sieve[i]:
            for j in range(2*i, N+1, i):
                sieve[j] = False

    superP, k = [], 0
    for i in range(N):
        if sieve[i]:
            k += 1
            if sieve[k]:
                superP.append(i)

    T = int(input())
    for _ in range(T):
        n = int(input())
        print(superP[n-1])


if __name__ == "__main__":
    main()
