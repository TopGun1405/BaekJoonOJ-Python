def main():
    ans = 0
    for i in range(4):
        puzzle = list(input())
        for j in range(4):
            if puzzle[j] != '.':
                ans += abs((ord(puzzle[j]) - ord('A')) % 4 - j)
                ans += abs((ord(puzzle[j]) - ord('A')) // 4 - i)
    print(ans)


if __name__ == "__main__":
    main()
