def main():
    def matMul(mat1: list, mat2: list) -> list:
        mat = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    mat[i][j] += mat1[i][k] * mat2[k][j] % 1_000
        return mat

    def matPow(mat: list, n: int) -> list:
        if n == 1:
            return mat
        tmpMat = matPow(mat, n // 2)
        if n % 2:
            return matMul(matMul(tmpMat, tmpMat), mat)
        else:
            return matMul(tmpMat, tmpMat)

    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    resMat = matPow(matrix, B)
    for row in resMat:
        print(*map(lambda k: k % 1_000, row))


if __name__ == "__main__":
    main()
