def main():
    T = int(input())

    for _ in range(T):
        n = int(input())

        maxN = n
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n *= 3
                n += 1
            maxN = max(maxN, n)

        print(maxN)


if __name__ == "__main__":
    main()
