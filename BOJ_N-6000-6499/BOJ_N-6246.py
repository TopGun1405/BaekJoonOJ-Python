def main():
    N, Q = map(int, input().split())

    balloons = [0] * N
    for _ in range(Q):
        L, I = map(int, input().split())

        for i in range(L-1, N, I):
            balloons[i] = 1

    print(N - sum(balloons))


if __name__ == "__main__":
    main()
