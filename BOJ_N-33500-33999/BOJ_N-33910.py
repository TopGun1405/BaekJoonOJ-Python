def main():
    N = int(input())
    A = list(map(int, input().split()))

    minSum = A[-1]
    for i in range(N-2, -1, -1):
        if A[i] > A[i+1]:
            A[i] = A[i+1]
            minSum += A[i+1]
        else:
            minSum += A[i]

    print(minSum)


if __name__ == "__main__":
    main()
