def MenOfPassion(A: list, n: int):
    tot = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            # code 1
            tot = tot + A[i] * A[j]
    return tot


def main():
    n = int(input())
    print(n * (n - 1) // 2)
    print(2)


if __name__ == "__main__":
    main()
