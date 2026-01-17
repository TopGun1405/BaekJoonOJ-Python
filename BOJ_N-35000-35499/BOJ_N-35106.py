def main():
    N = int(input())
    rounds = list(map(int, input().split()))

    hands = {1: N, 2: N, 3: N}
    wrong_hand = 0
    for i in range(3*N):
        if hands[rounds[i]] > 0:
            hands[rounds[i]] -= 1
        else:
            wrong_hand = rounds[i]

    print(list(filter(lambda e: e[1] == 1, hands.items()))[0][0])
    print(wrong_hand)


if __name__ == "__main__":
    main()
