def main():
    N, K, P = map(int, input().split())
    cream = list(map(int, input().split()))

    sellable = 0
    for i in range(N):
        cnt = 0
        for j in range(K):
            if cream[i*K+j] == 0:
                cnt += 1
        if cnt < P:
            sellable += 1

    print(sellable)


if __name__ == "__main__":
    main()
