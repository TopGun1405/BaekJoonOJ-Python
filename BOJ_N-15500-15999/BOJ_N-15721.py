def main():
    A = int(input())
    T = int(input())
    S = int(input())

    B, D = 1, 1
    game_cnt = 0
    games = []
    while True:
        n, game_cnt = B, game_cnt + 1

        for _ in range(2):
            games.append([B, 0])
            B += 1
            games.append([D, 1])
            D += 1

        for _ in range(game_cnt+1):
            games.append([B, 0])
            B += 1

        for _ in range(game_cnt+1):
            games.append([D, 1])
            D += 1

        if n <= T < B:
            print(games.index([T, S]) % A)
            break


if __name__ == "__main__":
    main()
