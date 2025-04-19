def main():
    n = int(input())
    d = list(map(int, input().split()))

    maxB = 0
    for i in range(n-1):
        B = max(d[i:])
        maxB = max(maxB, B-d[i])

    print(maxB)


if __name__ == "__main__":
    main()
