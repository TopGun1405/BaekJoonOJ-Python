def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    M = int(input())

    cost = 0
    for _ in range(M):
        Bj = int(input())
        cost += A[Bj-1]

    print(cost)


if __name__ == "__main__":
    main()
