def main():
    n = int(input())
    for _ in range(n):
        board = list(map(int, input().split()))

        row = {r: 0 for r in range(1, 9)}
        for y in range(2, len(board), 2):
            row[board[y]] += 1
        row = sorted(row.values(), reverse=True)

        print(row[0])


if __name__ == "__main__":
    main()
