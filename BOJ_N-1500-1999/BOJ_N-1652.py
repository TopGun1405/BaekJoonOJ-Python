def main():
    N: int = int(input())
    room: list = [input() for _ in range(N)]

    seat: list = [0, 0]
    for i in range(N):
        r, c = 0, 0
        for j in range(N):
            r = (r + 1) if room[i][j] == '.' else 0
            if r == 2:
                seat[0] += 1

            c = (c + 1) if room[j][i] == '.' else 0
            if c == 2:
                seat[1] += 1
    print(*seat)


if __name__ == "__main__":
    main()
