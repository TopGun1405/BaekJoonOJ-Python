def main():
    W, N = map(lambda e: int(e) if e.isdigit() else e, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    rev = {1: 1, 2: 5, 3: "?", 4: "?",
           5: 2, 6: "?", 7: "?", 8: 8, 9: "?"}
    if W == "L" or W == "R":
        for i in range(N):
            print(*map(lambda n: rev[n], board[i][::-1]))
    elif W == "U" or W == "D":
        for i in range(N-1, -1, -1):
            print(*map(lambda n: rev[n], board[i]))


if __name__ == "__main__":
    main()
