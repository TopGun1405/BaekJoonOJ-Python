def main():
    aCard = list(map(int, input().split()))
    bCard = list(map(int, input().split()))
    A = B = 0
    for i in range(10):
        if aCard[i] > bCard[i]:
            A += 1
        elif aCard[i] < bCard[i]:
            B += 1
    print('A' if A > B else 'B' if A < B else 'D')


if __name__ == "__main__":
    main()
