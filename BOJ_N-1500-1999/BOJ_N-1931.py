def main():
    N = int(input())
    mTime = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda k: (k[1], k[0]))
    meeting, endTime = 1, mTime[0][1]
    for i in range(1, N):
        if mTime[i][0] >= endTime:
            meeting, endTime = meeting + 1, mTime[i][1]
    print(meeting)


if __name__ == "__main__":
    main()
