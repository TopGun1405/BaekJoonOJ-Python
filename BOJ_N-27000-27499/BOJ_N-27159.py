def main():
    N = int(input())
    x = list(map(int, input().split()))
    s = x[0]
    score = 0
    for i in range(1, N):
        if x[i] - x[i - 1] != 1:
            score += s
            s = x[i]
    print(score + s)


if __name__ == "__main__":
    main()
