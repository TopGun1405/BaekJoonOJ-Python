def main():
    Z = int(input())
    for _ in range(Z):
        n = int(input())
        ways = input()

        dirs = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
        for w in ways:
            dirs[w] += 1

        print(abs(dirs['N'] - dirs['S']) + abs(dirs['W'] - dirs['E']))


if __name__ == "__main__":
    main()
