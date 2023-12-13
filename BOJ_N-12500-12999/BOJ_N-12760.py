def main():
    N, M = map(int, input().split())
    # cards = [sorted(map(int, input().split()), reverse=True) for _ in range(N)]
    cards = [sorted(map(int, input().split())) for _ in range(N)]

    players = {n: 0 for n in range(1, N + 1)}
    # for i in range(M):
    for i in range(M-1, -1, -1):
        battle = [cards[n][i] for n in range(N)]

        winners = list(
            map(lambda n: n[0],
                filter(lambda c: c[1] == max(battle),
                       enumerate(battle))))

        for winner in winners:
            players[winner + 1] += 1

    print(*map(lambda n: n[0],
               filter(lambda e: e[1] == max(players.values()),
                      players.items())))


if __name__ == "__main__":
    main()
