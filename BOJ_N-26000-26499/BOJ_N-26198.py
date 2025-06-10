def main():
    T = int(input())
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
           'C': 100, 'D': 500, 'M': 1_000}
    for _ in range(T):
        chronogram = input()

        year = 0
        for c in chronogram:
            try:
                year += val[c]
            except KeyError:
                continue

        print(year)


if __name__ == "__main__":
    main()
