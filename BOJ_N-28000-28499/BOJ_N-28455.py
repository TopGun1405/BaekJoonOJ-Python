def main():
    N = int(input())
    L = sorted([int(input()) for _ in range(N)], reverse=True)

    total_lv, st = 0, 0
    for lv in L[:42]:
        total_lv += lv
        if lv >= 250:
            st += 5
        elif lv >= 200:
            st += 4
        elif lv >= 140:
            st += 3
        elif lv >= 100:
            st += 2
        elif lv >= 60:
            st += 1
    print(total_lv, st)


if __name__ == "__main__":
    main()
