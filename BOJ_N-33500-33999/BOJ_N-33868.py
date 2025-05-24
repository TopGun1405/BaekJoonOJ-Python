def main():
    N = int(input())
    maxT, minB = 1, 5_000
    for _ in range(N):
        T, B = map(int, input().split())
        maxT, minB = max(maxT, T), min(minB, B)

    print((maxT * minB) % 7 + 1)


if __name__ == "__main__":
    main()
