def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(min(map(lambda ai: (ai[0] + ai[1]) * M, zip(A[:-1], A[1:]))))


if __name__ == "__main__":
    main()
