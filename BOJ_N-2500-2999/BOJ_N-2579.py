def main():
    N = int(input())
    stairs = [0] + [int(input()) for _ in range(N)]
    points = [0, stairs[1]] + [0] * (N - 1)
    for i in range(2, N + 1):
        points[i] = max(stairs[i] + points[i - 2], stairs[i] + stairs[i - 1] + points[i - 3])
    print(points[N])


if __name__ == "__main__":
    main()
