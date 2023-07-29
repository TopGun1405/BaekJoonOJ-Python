def main():
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda k: k[0])

    minTime = 0
    for time in times:
        A, B = time
        minTime = (A + B) if A >= minTime else (minTime + B)
    print(minTime)


if __name__ == "__main__":
    main()
