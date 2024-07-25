from itertools import combinations


def main():
    N = int(input())

    cards = []
    for i in range(N):
        card = list(map(int, input().split()))
        cards.append([i + 1, max([sum(case) % 10 for case in combinations(card, 3)])])
    cards.sort(key=lambda k: (k[1], k[0]), reverse=True)

    print(cards[0][0])


if __name__ == "__main__":
    main()
