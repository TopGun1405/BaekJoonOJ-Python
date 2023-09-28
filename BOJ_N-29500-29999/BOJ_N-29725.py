def main():
    board = [input() for _ in range(8)]
    white = {'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}
    black = {'k': 0, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}

    scoreW, scoreB = 0, 0
    for r in board:
        for c in r:
            try:
                scoreW += white[c]
            except KeyError:
                pass
            try:
                scoreB += black[c]
            except KeyError:
                pass
    print(scoreW - scoreB)


if __name__ == "__main__":
    main()
