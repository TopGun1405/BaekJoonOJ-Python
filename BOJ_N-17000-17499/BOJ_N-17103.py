def main():
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    maxN = max(nums)

    primes = [True] * (maxN + 1)
    for i in range(2, int(maxN ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, maxN + 1, i):
                if primes[j]:
                    primes[j] = False

    for n in nums:
        ans = 0
        for i in range(2, n // 2 + 1):
            if primes[i] and primes[n - i]:
                ans += 1
        print(ans)


if __name__ == "__main__":
    main()
