def main():

    # incomplete

    def pushBoard(board: list, side: int) -> list:
        cursor = [0, N-1]
        cursor_step = [1, -1]
        row, col = 0, 0
        start, end, step = [1, N-2], [N, -1], [1, -1]
        for i in range(N):
            for j in range(start[side], end[side], step[side]):
                pass

        return board

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

    def getMaxBlock(board: list) -> int:
        maxBlock = 0
        for row in board:
            maxBlock = max(max(row), maxBlock)

        return maxBlock

    def compareBoard(board: list) -> bool:
        return False

    def game2048(rec, board):
        # for row in board:
        #     print(*row)
        # print()

        maxVal = getMaxBlock(board)
        if maxVal < maxVal * (2 ** (10 - rec)):
            return

        if rec == 10:
            block['MAX'] = max(getMaxBlock(board), block['MAX'])
            return

        for i in range(4):
            copied_board = [row[::] for row in board]
            game2048(rec+1, pushBoard(copied_board, i % 2))
            # if i == 0:
            #     game2048(rec+1, pushUp(copied_board))
            # elif i == 1:
            #     game2048(rec+1, pushDown(copied_board))
            # elif i == 2:
            #     game2048(rec+1, pushLeft(copied_board))
            # else:
            #     game2048(rec+1, pushRight(copied_board))

    N = int(input())
    original_board = [list(map(int, input().split())) for _ in range(N)]

    block = {'MAX': 0}
    game2048(0, original_board)

    print(block['MAX'])


if __name__ == "__main__":
    main()
