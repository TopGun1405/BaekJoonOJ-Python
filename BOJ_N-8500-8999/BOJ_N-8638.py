def main():
    N = int(input())
    score = list(map(int, input().split()))
    maxScore = max(score)

    players = [[chr(n), k] for n, k in zip(range(65, 65+N), score)]
    nextRoundPlayer = list(map(lambda c: c[0], filter(lambda e: e[1] == maxScore, players)))

    print("".join(nextRoundPlayer))


if __name__ == "__main__":
    main()
