def main():
    game = list(input())
    player = {'A': 0, 'B': 0}
    i = 0
    while i < len(game):
        player[game[i]] += int(game[i + 1])
        i += 2
    print('A' if player['A'] > player['B'] else 'B')


if __name__ == "__main__":
    main()
