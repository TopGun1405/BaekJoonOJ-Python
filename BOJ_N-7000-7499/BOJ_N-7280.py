def main():
    cards = set([(c, n) for c in ["S", "B", "V", "K"] for n in range(1, 14)])
    for _ in range(51):
        card = input().split()
        cards.remove((card[0], int(card[1])))

    print(*list(cards)[0])


if __name__ == "__main__":
    main()
