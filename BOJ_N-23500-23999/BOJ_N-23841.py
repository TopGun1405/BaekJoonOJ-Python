def main():
    N, M = map(int, input().split())
    pics = [list(input()) for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if pics[n][m] != '.':
                pics[n][-m-1] = pics[n][m]

    for pic in pics:
        print(*pic, sep='')


if __name__ == "__main__":
    main()
