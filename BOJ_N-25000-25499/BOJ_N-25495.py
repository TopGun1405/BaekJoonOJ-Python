def main():
    N = int(input())
    A = list(map(int, input().split()))
    useB, currB, currP = 0, 0, 0
    for a in A:
        if currP == a:
            useB *= 2
        else:
            currP = a
            useB = 2
        currB += useB
        if currB >= 100:
            useB, currB, currP = 0, 0, 0
    print(currB)


if __name__ == "__main__":
    main()
