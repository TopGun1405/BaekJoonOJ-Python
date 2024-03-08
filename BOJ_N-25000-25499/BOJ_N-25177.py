def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N < M:
        a += [0] * (M - N)

    maxVal = 0
    for i in range(M):
        maxVal = max(maxVal, b[i] - a[i])

    print(maxVal)


if __name__ == "__main__":
    main()
