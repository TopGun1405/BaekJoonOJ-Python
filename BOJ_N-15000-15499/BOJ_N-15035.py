def main():
    N = int(input())
    H = list(map(int, input().split()))
    T = int(input())

    minWaste, setting = 500, -1
    for Hi in H:
        waste = T % Hi
        if waste < minWaste:
            minWaste, setting = waste, Hi
    print(setting)


if __name__ == "__main__":
    main()
