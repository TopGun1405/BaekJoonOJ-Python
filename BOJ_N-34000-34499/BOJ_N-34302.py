def main():
    N = int(input())

    maxS, currS = 0, 0
    for _ in range(N):
        S, T = map(int, input().split())

        if S > T:
            currS += 1
            maxS = max(maxS, currS)
        else:
            currS = 0

    print(maxS)


if __name__ == "__main__":
    main()
