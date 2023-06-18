def main():
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))
    print(A[K - 1])


if __name__ == "__main__":
    main()
