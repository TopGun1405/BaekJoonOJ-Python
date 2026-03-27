def main():
    s = input()

    alp = {}
    for c in s:
        try:
            alp[c] += 1
        except KeyError:
            alp[c] = 1

    odd = list(filter(lambda e: e % 2, alp.values()))

    print((len(odd) - 1 if len(odd) > 1 else 0))


if __name__ == "__main__":
    main()
