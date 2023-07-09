def main():
    while True:
        SlowSpeed, MinWeight, MinStrength = map(float, input().split())
        if SlowSpeed == MinWeight == MinStrength == 0:
            break
        check = [lambda sp, mw, ms: sp <= 4.5 and mw >= 150 and ms >= 200,
                 lambda sp, mw, ms: sp <= 6.0 and mw >= 300 and ms >= 500,
                 lambda sp, mw, ms: sp <= 5.0 and mw >= 200 and ms >= 300]
        fill = []
        if SlowSpeed <= 4.5 and MinWeight >= 150 and MinStrength >= 200:
            fill.append("Wide Receiver")
        if SlowSpeed <= 6.0 and MinWeight >= 300 and MinStrength >= 500:
            fill.append("Lineman")
        if SlowSpeed <= 5.0 and MinWeight >= 200 and MinStrength >= 300:
            fill.append("Quarterback")
        print(' '.join(fill) if fill else "No positions")


if __name__ == "__main__":
    main()
