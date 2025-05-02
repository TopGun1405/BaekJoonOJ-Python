def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(N-1):
        if A[i] < A[i+1]:
            continue
        A[i+1] += K
        cnt += 1

    sign = 0
    for i in range(N-1):
        if A[i] < A[i+1]:
            continue
        sign = 1
        break

    print(cnt if sign == 0 else -1)


if __name__ == "__main__":
    main()
