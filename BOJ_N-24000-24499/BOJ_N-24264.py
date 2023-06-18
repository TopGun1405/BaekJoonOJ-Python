def MenOfPassion(A: list, n: int):
    tot = 0
    for i in range(n):
        for j in range(n):
            tot = tot + A[i] * A[j]
    return tot


def main():
    n = int(input())
    print(n ** 2)
    print(2)


if __name__ == "__main__":
    main()
