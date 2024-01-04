def main():
    N = int(input())
    slimes = sorted(map(int, input().split()), reverse=True)

    totalScore = 0
    for i in range(N - 1):
        score = slimes[i] * slimes[i+1]
        slimes[i+1] += slimes[i]
        totalScore += score
    print(totalScore)


if __name__ == "__main__":
    main()
