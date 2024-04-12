def main():
    R, B = map(int, input().split())
    LpW, LW = (R + 4) // 2, R + B

    for i in range(1, LpW):
        lw = LpW - i
        if lw * i != LW:
            continue
        print(max(i, lw), min(i, lw))
        break


if __name__ == "__main__":
    main()
