def main():
    N, M = map(int, input().split())
    S = set(input() for _ in range(N))
    find = [input() for _ in range(M)]
    count = 0

    for c in range(M):
        if find[c] in S:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
