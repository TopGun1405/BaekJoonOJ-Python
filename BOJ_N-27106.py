def main():
    P = int(input())
    P = 100 - P
    coins = {25: 0, 10: 0, 5: 0, 1: 0}
    for coin in coins:
        if P // coin > 0:
            coins[coin] = P // coin
            P %= coin
    print(*coins.values())


if __name__ == "__main__":
    main()
