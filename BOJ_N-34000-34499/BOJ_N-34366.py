def main():
    M = int(input())
    maxS, minS, maxT, minT = 0, int(1e9), 0, int(1e9)
    for _ in range(M):
        n = list(map(int, input().split()))
        S, score = n[0], n[1:]

        total = sum(score)
        maxS, minS = max(max(score), maxS), min(min(score), minS)
        maxT, minT = max(total, maxT), min(total, minT)

    print(maxS)
    print(minS)
    print(maxT)
    print(minT)


if __name__ == "__main__":
    main()
