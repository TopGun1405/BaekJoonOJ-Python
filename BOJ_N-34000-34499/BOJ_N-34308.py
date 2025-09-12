def main():
    N, K = map(int, input().split())
    apples = list(map(int, input().split()))

    buy = []
    for a in apples:
        if abs(N - a) < abs(a - 1):
            buy.append(N)
        else:
            buy.append(1)

    print(*buy)


if __name__ == "__main__":
    main()
