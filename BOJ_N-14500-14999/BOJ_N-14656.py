def main():
    N = int(input())
    student = list(map(int, input().split()))
    wrongNum = 0
    for i in range(N):
        if student[i] != i + 1:
            wrongNum += 1
    print(wrongNum)


if __name__ == "__main__":
    main()
