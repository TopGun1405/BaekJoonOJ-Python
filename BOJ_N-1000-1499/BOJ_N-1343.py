def main():
    board = input()

    board = board.replace("XXXX", "AAAA").replace("XX", "BB")
    print(-1 if 'X' in board else board)


if __name__ == "__main__":
    main()
