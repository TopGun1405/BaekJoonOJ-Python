def main():
    N, M = map(int, input().split())
    mat1 = [list(map(int, input().split())) for _ in range(N)]
    mat2 = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            print(mat1[i][j] + mat2[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
