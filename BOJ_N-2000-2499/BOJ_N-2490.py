def main():
    for _ in range(3):
        y = list(map(int, input().split()))
        game = {0: 'E', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
        print(game[y.count(0)])


if __name__ == "__main__":
    main()
