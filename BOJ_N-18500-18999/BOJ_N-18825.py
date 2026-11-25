def main():
    # n = 1332
    # sieve = [True] * (n+3)
    # for i in range(2, int(n**0.5)+1):
    #     if not sieve[i]:
    #         continue
    #     for j in range(2*i, n+3, i):
    #         sieve[j] = False
    #
    # p, k = n+2, 0
    # for i in range(2, n+3):
    #     if sieve[i] and (n+2) % i == 0:
    #         p = min(i, p)
    #         k += 1
    #         break
    #     if sieve[i]:
    #         k += 1
    #
    # print(p, k)
    # -> 1000번
    A, B = map(int, input().split())
    print(A + B)


if __name__ == "__main__":
    main()
