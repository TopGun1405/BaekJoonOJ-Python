def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxArr, minArr = [1] * N, [0] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                maxArr[i] = max(maxArr[i], maxArr[j] + 1)
            if A[-i-1] > A[-j-1]:
                minArr[i] = max(minArr[i], minArr[j] + 1)
    res = [maxArr[i] + minArr[-i-1] for i in range(N)]
    print(max(res))


if __name__ == "__main__":
    main()
