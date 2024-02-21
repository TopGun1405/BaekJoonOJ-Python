def main():
    R, C = map(int, input().split())
    A, B = map(int, input().split())

    board = []
    for r in range(R):
        if r % 2 == 0:
            for a in range(A):
                board.append([("." if c % 2 else "X") * B for c in range(C)])
        else:
            for a in range(A):
                board.append([("X" if c % 2 else ".") * B for c in range(C)])

    for row in board:
        print("".join(row))


if __name__ == "__main__":
    main()
