def main():
    N, M = map(int, input().split())

    streaks, names = [], []
    for _ in range(N):
        rec = input().split()

        streak, name = rec[:-1], rec[-1]
        maxS, currS = 0, 0
        for s in streak:
            if s == ".":
                currS += 1
            else:
                maxS = max(maxS, currS)
                currS = 0
        maxS = max(maxS, currS)

        streaks.append(maxS)
        names.append(name)

    print(len(set(streaks)))
    for s, n in zip(streaks, names):
        print(s, n)


if __name__ == "__main__":
    main()
