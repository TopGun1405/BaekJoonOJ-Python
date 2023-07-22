def main():
    B, C, D = map(int, input().split())
    BPrice = sorted(map(int, input().split()), reverse=True)
    SPrice = sorted(map(int, input().split()), reverse=True)
    DPrice = sorted(map(int, input().split()), reverse=True)

    cost, k = 0, min(B, C, D)
    for i in range(k):
        cost += (BPrice[i] + SPrice[i] + DPrice[i]) * 0.9
    cost += sum(BPrice[k:]) + sum(SPrice[k:]) + sum(DPrice[k:])

    print(sum(BPrice) + sum(SPrice) + sum(DPrice))
    print(int(cost))


if __name__ == "__main__":
    main()
