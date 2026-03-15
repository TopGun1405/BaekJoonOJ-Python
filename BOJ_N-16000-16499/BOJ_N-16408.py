def main():
    cards = input().split()

    ranks = {}
    for card in cards:
        rank, suit = card
        try:
            ranks[rank] += 1
        except KeyError:
            ranks[rank] = 1

    print(max(ranks.values()))


if __name__ == "__main__":
    main()
