def main():
    N = int(input())

    prices = []
    for _ in range(N):
        dice = sorted(map(int, input().split()))

        price = 0
        if len(set(dice)) == 1:
            price = 50_000 + 5_000 * dice[0]
        elif len(set(dice)) == 2:
            if dice[1] == dice[2]:
                price = 10_000 + 1_000 * dice[1]
            else:
                price = 2_000 + (dice[1] + dice[2]) * 500
        elif len(set(dice)) == 4:
            price = dice[-1] * 100
        else:
            for i in range(3):
                if dice[i] == dice[i+1]:
                    price = 1_000 + 100 * dice[i]
                    break
        prices.append(price)

    print(max(prices))


if __name__ == "__main__":
    main()
