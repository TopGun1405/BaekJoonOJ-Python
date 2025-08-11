def main():
    n = int(input())
    m = int(input())
    cards = list(range(1, 2*n+1))
    for _ in range(m):
        k = int(input())

        if k == 0:
            shuffle = []
            for c1, c2 in zip(cards[:n], cards[n:]):
                shuffle.append(c1)
                shuffle.append(c2)
            cards = shuffle
        else:
            cards = cards[k:] + cards[:k]

    print(*cards, sep="\n")


if __name__ == "__main__":
    main()
