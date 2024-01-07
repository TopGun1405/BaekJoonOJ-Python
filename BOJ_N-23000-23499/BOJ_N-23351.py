def main():
    N, K, A, B = map(int, input().split())
    pots = [K] * N
    days = 0
    while pots[0] > 0:
        for i in range(A):
            pots[i] += B
        for i in range(N):
            pots[i] -= 1
        pots.sort()
        days += 1
    print(days)


if __name__ == "__main__":
    main()
