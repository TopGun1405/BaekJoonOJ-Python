def main():
    N = int(input())

    times = [4, 6, 4, 10]
    schedule = {}
    for _ in range(N):
        work_tables = [input().split() for _ in range(4)]

        for i in range(7):
            for j in range(4):
                try:
                    schedule[work_tables[j][i]] += times[j]
                except KeyError:
                    if work_tables[j][i] == "-":
                        continue
                    schedule[work_tables[j][i]] = times[j]
    schedule = sorted(schedule.items(), key=lambda k: k[1])

    print("Yes" if not schedule or schedule[-1][1] - schedule[0][1] <= 12 else "No")


if __name__ == "__main__":
    main()
