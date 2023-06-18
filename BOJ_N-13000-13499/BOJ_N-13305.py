def main():
    N = int(input())
    roadLen = list(map(int, input().split()))
    gasPrice = list(map(int, input().split()))
    minPrice, totPrice = gasPrice[0], 0
    for i in range(N - 1):
        minPrice = min(minPrice, gasPrice[i])
        totPrice += minPrice * roadLen[i]
    print(totPrice)


if __name__ == "__main__":
    main()
