def main():
    A, B, C, M = map(int, input().split())

    day, works, cnt = 0, 0, 0
    if A > M:
        print(0)
    else:
        while day != 24:
            day += 1
            if cnt + A <= M:
                works, cnt = works + B, cnt + A
            else:
                cnt = cnt - C if cnt - C >= 0 else 0
        print(works)


if __name__ == "__main__":
    main()
