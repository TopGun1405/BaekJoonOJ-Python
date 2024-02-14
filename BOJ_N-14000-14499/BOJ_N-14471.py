def main():
    N, M = map(int, input().split())

    cards, cost = [], 0
    for _ in range(M):
        A, B = map(int, input().split())
        if A < N:
            cards.append([A, B])
        else:
            cost += 1

    cards.sort(reverse=True)
    print(0 if M - 1 == cost else sum(map(lambda card: N - card[0], cards[:M-1-cost])))


if __name__ == "__main__":
    main()
