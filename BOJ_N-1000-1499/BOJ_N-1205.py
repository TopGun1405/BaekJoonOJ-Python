def main():
    N, C, P = map(int, input().split())

    if N == 0:
        print(1)
    else:
        scores = list(map(int, input().split()))

        if N == P and scores[-1] >= C:
            print(-1)
        else:
            rank = N + 1
            for i, score in enumerate(scores):
                if score <= C:
                    rank = i + 1
                    break
            print(rank)


if __name__ == "__main__":
    main()
