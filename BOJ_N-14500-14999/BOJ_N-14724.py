def main():
    N = int(input())
    clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
    maxVals = []
    for _ in range(9):
        maxVals.append(max(map(int, input().split())))
    k = max(maxVals)
    for i, v in enumerate(maxVals):
        if k == v:
            print(clubs[i])
            break


if __name__ == "__main__":
    main()
