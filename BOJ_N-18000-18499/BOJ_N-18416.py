def main():
    N = int(input())
    A = list(map(int, input().split()))

    length, maxLength = 1, 1
    prev = A[0]
    for A_i in A[1:]:
        if A_i >= prev:
            length += 1
        else:
            maxLength = max(maxLength, length)
            length = 1
        prev = A_i
    maxLength = max(maxLength, length)

    print(maxLength)


if __name__ == "__main__":
    main()
