def main():
    N, M = map(int, input().split())
    tMap = [input() for _ in range(N)]

    t = 0
    for j in range(M):
        for i in range(N):
            if tMap[i][j] == "O":
                break
        else:
            t = j + 1
            break

    print(t if t else "ESCAPE FAILED")


if __name__ == "__main__":
    main()
