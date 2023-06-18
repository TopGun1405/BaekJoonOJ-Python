def MenOfPassion(A: list, n: int):
    tot = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # code 1
                tot = tot + A[i] * A[j] * A[k]
    return tot


def main():
    n = int(input())
    print(n ** 3)
    print(3)


if __name__ == "__main__":
    main()
