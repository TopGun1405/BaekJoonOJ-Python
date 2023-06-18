def main():
    N, M = map(int, input().split())
    basket = [n for n in range(1, N + 1)]
    for _ in range(M):
        i, j, k = map(int, input().split())
        basket[i-1:j] = basket[k-1:j] + basket[i-1:k-1]
    print(*basket)


if __name__ == "__main__":
    main()
