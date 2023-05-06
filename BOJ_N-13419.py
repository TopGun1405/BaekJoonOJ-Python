def main():
    T = int(input())
    games = [input() for _ in range(T)]
    for game in games:
        if len(game) % 2 == 0:
            print(game[0::2])
            print(game[1::2])
        else:
            print(game[0::2] + game[1::2])
            print(game[1::2] + game[0::2])


if __name__ == "__main__":
    main()
