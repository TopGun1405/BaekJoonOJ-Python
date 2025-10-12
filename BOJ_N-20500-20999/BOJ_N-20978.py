def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = sorted(set(A[i] for i in range(N) for j in range(M) if A[i] == B[j]))

    print(*AB, sep="\n")


if __name__ == "__main__":
    main()
