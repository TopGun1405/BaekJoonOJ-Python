def main():
    grid = [
        [1, 2],
        [3, 4]
    ]

    flip = input()

    if flip.count("H") % 2 == 1:
        grid[0], grid[1] = grid[1], grid[0]
    if flip.count("V") % 2 == 1:
        grid[0], grid[1] = grid[0][::-1], grid[1][::-1]

    for row in grid:
        print(*row)


if __name__ == "__main__":
    main()
