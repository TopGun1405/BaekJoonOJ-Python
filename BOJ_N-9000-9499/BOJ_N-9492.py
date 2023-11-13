def main():
    while True:
        n = int(input())
        if n == 0:
            break
        cards = [input() for _ in range(n)]

        m = len(cards) // 2
        k = 1 if len(cards) % 2 else 0

        shuffled = []
        for c1, c2 in zip(cards[:m], cards[m+k:]):
            shuffled.append(c1)
            shuffled.append(c2)
        if k:
            shuffled.append(cards[-m-1])

        print(*shuffled, sep='\n')


if __name__ == "__main__":
    main()
