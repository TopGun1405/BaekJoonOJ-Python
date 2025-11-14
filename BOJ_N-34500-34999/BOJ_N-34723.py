def main():
    P, M, C = map(int, input().split())
    X = int(input())

    minVal = int(1e9)
    for p in range(1, P+1):
        for m in range(1, M+1):
            for c in range(1, C+1):
                minVal = min(abs((p + m) * (m + c) - X), minVal)

    print(minVal)


if __name__ == "__main__":
    main()
