def main():
    N = int(input())
    P = list(map(int, input().split()))

    cnt = 0
    streak = []
    for Pn in P:
        if Pn == 0:
            streak.append(cnt)
            cnt = 0
        else:
            cnt += 1
    if P[-1] != 0:
        streak.append(cnt)

    maxStreak, cnt = 0, (0 if len(streak) >= 2 else streak[0])
    for s1, s2 in zip(streak[:-1], streak[1:]):
        if s2 - s1 < 0:
            maxStreak = max(maxStreak, cnt)
            cnt = 0
        else:
            cnt += s2+s1
    maxStreak = max(maxStreak, cnt)
    print(maxStreak)

    print(streak)


if __name__ == "__main__":
    main()
