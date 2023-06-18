def main():
    N, M = map(int, input().split())
    allPoint = 0
    for _ in range(N):
        Xj = list(map(int, input().split()))
        if 0 not in Xj:
            allPoint += 1
    print(allPoint)


if __name__ == "__main__":
    main()
