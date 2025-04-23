def main():
    n = int(input())
    votes = {}
    for _ in range(n):
        name = input()

        try:
            votes[name] += 1
        except KeyError:
            votes[name] = 1

    votes = sorted(votes.items(), key=lambda k: (-k[1], k[0]))
    ranked = list(map(lambda c: c[0], filter(lambda e: e[1] == votes[0][1], votes)))

    print(*ranked, sep="\n")


if __name__ == "__main__":
    main()
