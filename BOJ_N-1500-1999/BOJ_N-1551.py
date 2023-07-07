def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split(',')))
    for _ in range(K):
        B = []
        for Ai, Aj in zip(A[:-1], A[1:]):
            B.append(Aj - Ai)
        A = B
        # A = [Aj - Ai for Ai, Aj in zip(A[:-1], A[1:])]
    print(','.join(map(str, A)))


if __name__ == "__main__":
    main()
