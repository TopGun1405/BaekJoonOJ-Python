def main():
    N = int(input())

    mid = []
    for _ in range(N):
        cows = sorted(map(int, input().split()))
        mid.append(cows[N//2])

    print(sorted(mid)[N//2])


if __name__ == "__main__":
    main()
