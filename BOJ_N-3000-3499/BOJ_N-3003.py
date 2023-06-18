def main():
    chess_piece = [1, 1, 2, 2, 2, 8]
    founded = list(map(int, input().split()))

    for i in range(6):
        print(chess_piece[i] - founded[i], end=' ')


if __name__ == "__main__":
    main()