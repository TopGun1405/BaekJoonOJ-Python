def main():
    n = int(input())
    minTime = 200
    for _ in range(n):
        ti, li = map(int, input().split())
        minTime = min(minTime, ti + li)
    print(minTime)


if __name__ == "__main__":
    main()
