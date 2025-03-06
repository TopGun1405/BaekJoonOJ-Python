def main():
    A = input()
    B = input()

    board = {chr(c): n for c, n in zip(range(97, 105), range(1, 9))}
    A_x, A_y = board[A[0]], int(A[1])
    B_x, B_y = board[B[0]], int(B[1])

    x, y = min(abs(A_x-B_x), abs(A_y-B_y)), max(abs(A_x-B_x), abs(A_y-B_y))
    print(x, y)


if __name__ == "__main__":
    main()
