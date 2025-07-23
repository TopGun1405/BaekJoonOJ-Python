def main():
    N, M, D = map(int, input().split())
    room = [list(input()) for _ in range(N)]

    cnt = 0
    if N >= D:
        for i in range(M):
            for j in range(N-D+1):
                for k in range(j, j+D):
                    if room[k][i] == "#":
                        break
                else:
                    cnt += 1

    if M >= D:
        for i in range(N):
            for j in range(M-D+1):
                if "#" not in room[i][j:j+D]:
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
