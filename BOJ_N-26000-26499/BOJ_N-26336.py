from math import gcd


def main():
    t = int(input())
    for _ in range(t):
        D, G, F = map(int, input().split())

        gas, food = (D-1)//G, (D-1)//F
        lcm = G * F // gcd(G, F)
        both = (D - 1) // lcm

        print(D, G, F)
        print(gas + food - both)


if __name__ == "__main__":
    main()
