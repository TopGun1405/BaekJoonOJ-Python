def main():
    N = int(input())
    guards, times = [], [0] * 1_001
    for _ in range(N):
        s, e = map(int, input().split())
        guards.append([s, e])
        for i in range(s, e):
            times[i] += 1

    maxT = 0
    for s, e in guards:
        tmp = times[::]
        for i in range(s, e):
            tmp[i] -= 1

        t = 0
        for n in tmp:
            if n > 0:
                t += 1

        maxT = max(t, maxT)

    print(maxT)


if __name__ == "__main__":
    main()
