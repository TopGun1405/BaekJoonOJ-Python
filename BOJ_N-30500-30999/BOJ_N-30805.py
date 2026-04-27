def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    intersection = set(A) & set(B)
    if not intersection:
        print(0)
    else:
        seq = []
        while intersection:
            maxVal = max(intersection)
            seq.append(maxVal)

            i, j = A.index(maxVal), B.index(maxVal)
            A, B = A[i+1:], B[j+1:]

            intersection = set(A) & set(B)

        print(len(seq))
        print(*seq)


if __name__ == "__main__":
    main()
