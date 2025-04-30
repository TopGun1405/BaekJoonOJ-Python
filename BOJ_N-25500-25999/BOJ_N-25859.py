def main():
    S = input()

    alp = {}
    for c in S:
        try:
            alp[c] += 1
        except KeyError:
            alp[c] = 1

    alp = sorted(alp.items(), key=lambda k: (-k[1], k[0]))

    for c, k in alp:
        print(c * k, end="")


if __name__ == "__main__":
    main()
