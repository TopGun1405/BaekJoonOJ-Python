from math import gcd


mod = 1_000_000_007


def main():

    def squaredNum(n, exp):
        if exp == 1:
            return n

        if exp % 2 == 0:
            half = squaredNum(n, exp//2)
            return half * half % mod
        else:
            return n * squaredNum(n, exp-1) % mod

    M = int(input())

    tot = 0
    for _ in range(M):
        N_i, S_i = map(int, input().split())

        GCD = gcd(N_i, S_i)
        N_i //= GCD
        S_i //= GCD

        tot += S_i * squaredNum(N_i, mod-2) % mod
        tot %= mod

    print(tot)


if __name__ == "__main__":
    main()
