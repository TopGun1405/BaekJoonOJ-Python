def main():
    N = int(input())
    cards = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}
    for _ in range(N):
        name, cnt = input().split()
        cards[name] += int(cnt)
    print(["NO", "YES"][5 in cards.values()])


if __name__ == "__main__":
    main()
