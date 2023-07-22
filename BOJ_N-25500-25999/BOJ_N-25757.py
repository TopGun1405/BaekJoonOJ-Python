def main():
    N, Game = map(lambda e: int(e) if e.isdigit() else e, input().split())
    players = set([input() for _ in range(N)])
    miniGame = {
        'Y': lambda n: n,
        'F': lambda n: n // 2,
        'O': lambda n: n // 3
    }
    print(miniGame[Game](len(players)))


if __name__ == "__main__":
    main()
