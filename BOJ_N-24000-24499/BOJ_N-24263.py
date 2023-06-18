def main():
    n = int(input())
    print(n)
    print(1)


def MenOfPassion(A, n):
    s = 0
    for i in range(n):
        s = s + A[i]
    return s


if __name__ == "__main__":
    main()
