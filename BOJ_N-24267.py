def MenOfPassion(A: list, n: int):
    tot = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                tot = tot + A[i] * A[j] * A[k]
    return tot


def main():
    n = int(input())
    print(n * (n - 1) * (n - 2) // 6)
    print(3)


if __name__ == "__main__":
    main()
