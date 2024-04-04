def main():
    def matMul(mat1: list, mat2: list) -> list:
        mat = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    mat[i][j] += mat1[i][k] * mat2[k][j] % 1_000_000_007
        return mat

    def matPow(mat: list, k: int) -> list:
        if k == 1:
            return mat
        tmpMat = matPow(mat, k // 2)
        if k % 2:
            return matMul(matMul(tmpMat, tmpMat), mat)
        else:
            return matMul(tmpMat, tmpMat)

    # 0 1
    # 1 1
    n = int(input())

    matrix = [[0, 1],
              [1, 1]]
    resMat = matPow(matrix, n)

    print(resMat[-1][0] % 1_000_000_007)


if __name__ == "__main__":
    main()
