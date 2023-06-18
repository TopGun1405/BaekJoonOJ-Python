def main():
    N, K = map(int, input().split())
    knapsack = [0] * (K + 1)
    for _ in range(N):
        W, V = map(int, input().split())
        for i in range(K, W - 1, -1):
            knapsack[i] = max(knapsack[i], knapsack[i - W] + V)
    print(knapsack[-1])


if __name__ == "__main__":
    main()
