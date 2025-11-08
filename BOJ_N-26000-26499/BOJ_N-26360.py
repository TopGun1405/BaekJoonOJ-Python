def main():
    X = int(input())
    S = int(input())
    F = int(input())

    score = 0
    if S == 1:
        score += X
    if F == 1:
        if S == 1:
            score += int(input())
        else:
            for _ in range(X):
                score += int(input())

    print(score)


if __name__ == "__main__":
    main()
