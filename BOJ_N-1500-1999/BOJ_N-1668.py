def main():
    N = int(input())
    trophy = [int(input()) for _ in range(N)]

    h, lCnt = trophy[0], 1
    for hi in trophy:
        if hi > h:
            h = hi
            lCnt += 1

    h, rCnt = trophy[-1], 1
    for hi in trophy[::-1]:
        if hi > h:
            h = hi
            rCnt += 1

    print(lCnt)
    print(rCnt)


if __name__ == "__main__":
    main()
