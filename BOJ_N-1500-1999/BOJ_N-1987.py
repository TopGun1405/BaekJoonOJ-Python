def main():

    def alphabet(r, c, currM):
        maxMove[0] = max(maxMove[0], currM)
        for i in range(4):
            currR = r + dx[i]
            currC = c + dy[i]
            if 0 <= currR < R and 0 <= currC < C:
                currA = ord(board[currR][currC]) - 65
                if alp[currA] == 0:
                    alp[currA] = 1
                    alphabet(currR, currC, currM + 1)
                    alp[currA] = 0

    R, C = map(int, input().split())
    board = [input().strip() for _ in range(R)]
    alp = [0 if i != ord(board[0][0]) - 65 else 1 for i in range(26)]
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    # delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    maxMove = [1]
    alphabet(0, 0, 1)
    print(*maxMove)


if __name__ == "__main__":
    main()
