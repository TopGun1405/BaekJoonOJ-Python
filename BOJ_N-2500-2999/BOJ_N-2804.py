def main():
    A, B = input().split()

    row, col = 0, 0
    for i in range(len(A)):
        if A[i] in B:
            row, col = B.index(A[i]), i
            break

    for i in range(len(B)):
        if i == row:
            print(A)
        else:
            print("." * col + B[i] + "." * (len(A) - col - 1))


if __name__ == "__main__":
    main()
