def main():
    cards = {'A': 4, 'K': 3, 'Q': 2, 'J': 1, 'X': 0}
    N = int(input())
    point = 0
    for _ in range(N):
        Ki = input()
        for ki in Ki:
            point += cards[ki]
    print(point)


if __name__ == "__main__":
    main()
