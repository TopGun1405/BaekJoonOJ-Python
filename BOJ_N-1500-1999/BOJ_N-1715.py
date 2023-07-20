from heapq import heappop, heappush


def main():
    N = int(input())
    cards = []
    for _ in range(N):
        heappush(cards, int(input()))

    if len(cards) == 1:
        print(0)
    else:
        cnt = 0
        while len(cards) > 1:
            comp = heappop(cards) + heappop(cards)
            cnt += comp
            heappush(cards, comp)
        print(cnt)


if __name__ == "__main__":
    main()
