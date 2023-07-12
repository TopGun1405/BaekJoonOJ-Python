def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = set(map(int, input().split()))

    boxList = {}
    for a in A:
        try:
            boxList[a] += 1
        except KeyError:
            boxList[a] = 1

    cnt = 0
    for b in B:
        try:
            cnt += boxList[b]
        except KeyError:
            continue
    print(cnt)


if __name__ == "__main__":
    main()
