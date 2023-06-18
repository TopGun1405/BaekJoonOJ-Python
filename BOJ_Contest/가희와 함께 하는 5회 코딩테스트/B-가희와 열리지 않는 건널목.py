def main():
    c, h = map(int, input().split())
    trains = sorted([list(map(int, input().split(':'))) for _ in range(c + h)])
    print(trains)
    ph, pm, ps = 0, 0, 0
    isClosedT = 0
    for times in trains:
        hh, mm, ss = times[0], times[1], times[2]
        cTimes = hh*1440 + mm*60 + ss
        pTimes = ph*1440 + pm*60 + ps
        print(pTimes, cTimes)
        print(ph, pm, ps, hh, mm, ss)
        print()
        if cTimes - pTimes < 40:
            isClosedT += cTimes - pTimes
        else:
            isClosedT += 40
        ph, pm, ps = hh, mm, ss
    print(86_400 - isClosedT)


if __name__ == "__main__":
    main()
