def main():
    N = int(input())
    p = list(map(int, input().split()))
    score = []
    if p[0] == 1:
        score.append(1)
    for i in range(1, len(p)):
        if p[i] == 1 and p[i - 1] == 1:
            score.append(score[-1] + 1)
        elif p[i] == 1 and p[i - 1] == 0:
            score.append(1)
    print(sum(score))


if __name__ == "__main__":
    main()
