def main():
    N = int(input())
    A = list(map(int, input().split()))
    length, maxLen = [1] * N, 1
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                length[i] = max(length[i], length[j] + 1)
                maxLen = max(maxLen, length[i])
    print(maxLen)


if __name__ == "__main__":
    main()
