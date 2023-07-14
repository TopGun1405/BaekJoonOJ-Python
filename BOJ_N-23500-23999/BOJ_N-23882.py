def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    exchange = 0
    for i in range(N-1, 0, -1):
        idx = A.index(max(A[:i+1]))

        if idx != i:
            A[idx], A[i] = A[i], A[idx]
            exchange += 1

        if exchange == K:
            print(*A)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
