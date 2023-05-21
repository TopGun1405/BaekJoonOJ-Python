def main():
    n, m, k = map(int, input().split())
    allChildren = set(range(1, n + 1))
    firstBag = set(map(int, input().split()))
    secondBag = set(map(int, input().split()))
    thirdBag = allChildren - firstBag - secondBag
    print(len(thirdBag))
    print(*thirdBag)


if __name__ == "__main__":
    main()
