def main():

    def roundT(n):
        return round(n + 10**(-len(str(n)) - 1))

    z = int(input())
    for _ in range(z):
        R, G, B = 0, 0, 0
        for _ in range(10):
            r, g, b = map(int, input().split())
            R, G, B = R + r, G + g, B + b
        print(roundT(R / 10), roundT(G / 10), roundT(B / 10))


if __name__ == "__main__":
    main()
