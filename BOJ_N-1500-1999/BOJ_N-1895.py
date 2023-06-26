def main():
    R, C = map(int, input().split())
    pixel = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())

    cnt = 0
    for r in range(R - 2):
        for c in range(C - 2):
            J = [pixel[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
            J.sort()
            if J[4] >= T:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
