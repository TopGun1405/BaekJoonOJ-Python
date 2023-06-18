def main():
    time = [list(map(int, input().split())) for _ in range(3)]

    for i in range(3):
        if time[i][5] - time[i][2] < 0:
            time[i][5] = time[i][5] + 60
            time[i][4] = time[i][4] - 1
        if time[i][4] - time[i][1] < 0:
            time[i][4] = time[i][4] + 60
            time[i][3] = time[i][3] - 1
        print(time[i][3] - time[i][0], time[i][4] - time[i][1], time[i][5] - time[i][2])


if __name__ == "__main__":
    main()
