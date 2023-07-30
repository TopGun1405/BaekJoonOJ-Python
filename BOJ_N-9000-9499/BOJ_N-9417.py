def gcd(m: int, n: int) -> int:
    m, n = max(m, n), min(m, n)
    if n == 0:
        return m
    if m % n == 0:
        return n
    return gcd(n, m % n)


def main():
    N = int(input())
    for _ in range(N):
        nums = list(map(int, input().split()))
        maxGCD = 0
        for i, a in enumerate(nums[:-1]):
            for b in nums[i+1:]:
                maxGCD = max(maxGCD, gcd(a, b))
        print(maxGCD)


if __name__ == "__main__":
    main()
