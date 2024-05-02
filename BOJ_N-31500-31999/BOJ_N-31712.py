def main():
    CU, DU = map(int, input().split())
    CD, DD = map(int, input().split())
    CP, DP = map(int, input().split())
    H = int(input())

    time = 0
    while True:
        if time % CU == 0:
            H -= DU
        if time % CD == 0:
            H -= DD
        if time % CP == 0:
            H -= DP

        if H <= 0:
            break
        time += 1

    print(time)


if __name__ == "__main__":
    main()
