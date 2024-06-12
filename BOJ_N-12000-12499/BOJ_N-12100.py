def main():

    def pushUp(board: list) -> list:
        for c in range(N):
            cursor = 0
            for r in range(N):
                if board[r][c] == 0:
                    continue

                current_block = board[r][c]
                board[r][c] = 0

                if board[cursor][c] == 0:
                    board[cursor][c] = current_block

                elif board[cursor][c] == current_block:
                    board[cursor][c] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[cursor][c] = current_block

        return board

    def pushDown(board: list) -> list:
        for c in range(N):
            cursor = N-1
            for r in range(N-1, -1, -1):
                if board[r][c] == 0:
                    continue

                current_block = board[r][c]
                board[r][c] = 0

                if board[cursor][c] == 0:
                    board[cursor][c] = current_block

                elif board[cursor][c] == current_block:
                    board[cursor][c] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    board[cursor][c] = current_block

        return board

    def pushLeft(board: list) -> list:
        for r in range(N):
            cursor = 0
            for c in range(N):
                if board[r][c] == 0:
                    continue

                current_block = board[r][c]
                board[r][c] = 0

                if board[r][cursor] == 0:
                    board[r][cursor] = current_block

                elif board[r][cursor] == current_block:
                    board[r][cursor] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[r][cursor] = current_block

        return board

    def pushRight(board: list) -> list:
        for r in range(N):
            cursor = N-1
            for c in range(N-1, -1, -1):
                if board[r][c] == 0:
                    continue

                current_block = board[r][c]
                board[r][c] = 0

                if board[r][cursor] == 0:
                    board[r][cursor] = current_block

                elif board[r][cursor] == current_block:
                    board[r][cursor] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    board[r][cursor] = current_block

        return board

    def game2048(rec, board):
        # for row in board:
        #     print(*row)
        # print()

        if rec == 5:
            for row in board:
                block['MAX'] = max(max(row), block['MAX'])
            return

        for i in range(4):
            copied_board = [row[::] for row in board]
            if i == 0:
                game2048(rec+1, pushUp(copied_board))
            elif i == 1:
                game2048(rec+1, pushDown(copied_board))
            elif i == 2:
                game2048(rec+1, pushLeft(copied_board))
            else:
                game2048(rec+1, pushRight(copied_board))

    N = int(input())
    original_board = [list(map(int, input().split())) for _ in range(N)]

    block = {'MAX': 0}
    game2048(0, original_board)

    print(block['MAX'])


if __name__ == "__main__":
    main()
