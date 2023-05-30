def main():
    p = int(input())
    tot = []
    players = {n: chr(65 + n) for n in range(p)}
    for i in range(p):
        cards = list(map(int, input().split()))
        c, cards = cards[0], list(map(lambda e: [i, e], cards[1:]))
        tot += cards
    tot.sort(key=lambda k: k[1])
    for p, card in tot:
        print(players[p], end='')


if __name__ == "__main__":
    main()
