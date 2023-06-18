def main():
    a, d, k = map(int, input().split())
    dn = k - a + d
    print(dn // d if dn % d == 0 and dn // d >= 1 else 'X')


if __name__ == "__main__":
    main()
