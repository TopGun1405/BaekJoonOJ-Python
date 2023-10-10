def main():
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]

    S = 0
    for [x1, y1], [x2, y2] in zip(pos, pos[1:] + [pos[0]]):
        S += x1*y2 - x2*y1
    print(abs(S) / 2)


if __name__ == "__main__":
    main()
