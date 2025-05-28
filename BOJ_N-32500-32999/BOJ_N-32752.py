def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    A = A[:L-1] + sorted(A[L-1:R]) + A[R:]

    print(1 if sorted(A) == A else 0)


if __name__ == "__main__":
    main()
