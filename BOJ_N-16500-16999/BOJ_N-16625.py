def main():

    def lcm(n, m):
        for k in range(max(n, m), (n * m) + 1):
            if k % n == k % m == 0:
                return k

    p, q, s = map(int, input().split())

    print("yes" if lcm(p, q) <= s else "no")


if __name__ == "__main__":
    main()
