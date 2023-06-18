def main():
    N = int(input())
    x = list(map(int, input().split()))

    score = [0] * 1_000_001
    cards = [0] * 1_000_001
    for xi in x:
        cards[xi] = 1

    for xi in sorted(x):
        for i in range(2 * xi, 1_000_001, xi):
            if cards[i]:
                score[i] -= 1
                score[xi] += 1

    for xi in x:
        print(score[xi], end=' ')


if __name__ == "__main__":
    main()
