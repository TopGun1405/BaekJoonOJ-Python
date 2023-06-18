def main():
    n = int(input())
    for _ in range(n):
        coins = list(map(int, input().split()))

        print("Denominations: ", end='')
        print(*coins[1:], sep=' ')
        prevCoin = coins[1]
        for coin in coins[2:]:
            if coin < prevCoin * 2:
                print("Bad coin denominations!")
                break
            prevCoin = coin
        else:
            print("Good coin denominations!")
        if _ < n:
            print()


if __name__ == "__main__":
    main()
