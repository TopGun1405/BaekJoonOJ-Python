def main():
    N = int(input())
    T = list(map(int, input().split()))
    totT = sum(T) + 8 * (N - 1)
    print(totT // 24, totT % 24)


if __name__ == "__main__":
    main()
