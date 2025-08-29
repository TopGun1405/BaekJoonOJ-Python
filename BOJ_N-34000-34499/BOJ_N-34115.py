def main():
    N = int(input())
    X = list(map(int, input().split()))

    cards = {}
    maxN = 0
    for i, X_i in enumerate(X):
        try:
            maxN = max(i-cards[X_i], maxN)
        except KeyError:
            cards[X_i] = i + 1

    print(maxN)


if __name__ == "__main__":
    main()
