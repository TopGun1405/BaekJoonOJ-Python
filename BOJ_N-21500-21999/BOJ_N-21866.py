def main():
    score = list(map(int, input().split()))
    maxScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]
    for i in range(len(score)):
        if score[i] > maxScore[i]:
            print("hacker")
            break
    else:
        if sum(score) >= 100:
            print("draw")
        else:
            print("none")


if __name__ == "__main__":
    main()
