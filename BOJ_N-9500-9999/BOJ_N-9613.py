from itertools import combinations


def gcd(m: int, n: int) -> int:
    while n != 0:
        m, n = n, m % n
    return abs(m)


def main():
    t = int(input())
    for _ in range(t):
        testcase = list(map(int, input().split()))
        total = 0
        for x, y in combinations(testcase[1:], 2):
            total += gcd(x, y)
        print(total)


if __name__ == "__main__":
    main()
