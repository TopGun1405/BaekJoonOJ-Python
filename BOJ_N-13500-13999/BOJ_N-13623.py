def main():
    zero_one = list(map(int, input().split()))
    game = {0: 'A', 1: 'B', 2: 'C'}
    if zero_one.count(0) == 1:
        print(game[zero_one.index(0)])
    elif zero_one.count(1) == 1:
        print(game[zero_one.index(1)])
    else:
        print('*')


if __name__ == "__main__":
    main()
