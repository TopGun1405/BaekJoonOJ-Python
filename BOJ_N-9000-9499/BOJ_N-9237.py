def main():
    N = int(input())
    t = sorted(map(int, input().split()), reverse=True)

    maxT = t[0]
    if N == 1:
        print(N + 2)
    else:
        for i in range(1, N):
            maxT = max(maxT, i + t[i])
        print(maxT + 2)


if __name__ == "__main__":
    main()
