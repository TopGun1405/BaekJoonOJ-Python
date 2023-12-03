def main():
    def getArmsLen(row: int, col: int) -> tuple:
        left, right = 0, 0

        C = col-1
        while 0 <= C and a[row][C] != "_":
            C -= 1
            left += 1

        C = col+1
        while C < N and a[row][C] != "_":
            C += 1
            right += 1

        return left, right

    def getWaistsLen(row: int, col: int) -> tuple:
        length = 0

        row += 1
        while a[row][col] != "_":
            row += 1
            length += 1

        return [row-1, col], length

    def getLegsLen(row: int, col: int) -> tuple:
        left, right = 0, 0

        R, C = row+1, col-1
        while R < N and a[R][C] != "_":
            R += 1
            left += 1

        R, C = row+1, col+1
        while R < N and a[R][C] != "_":
            R += 1
            right += 1

        return left, right

    N = int(input())
    a = [list(input()) for _ in range(N)]
    heart = [
        ["_", "*", "_"],
        ["*", "*", "*"],
        ["_", "*", "_"]
    ]

    for r in range(1, N-1):
        for c in range(1, N-1):
            block = [a[i][c-1:c+2] for i in range(r-1, r+2)]
            if block == heart:
                l_arm, r_arm = getArmsLen(r, c)
                w_pos, waist = getWaistsLen(r, c)
                l_leg, r_leg = getLegsLen(w_pos[0], w_pos[1])

                print(r+1, c+1)
                print(l_arm, r_arm, waist, l_leg, r_leg)
                break
        else:
            continue


if __name__ == "__main__":
    main()
