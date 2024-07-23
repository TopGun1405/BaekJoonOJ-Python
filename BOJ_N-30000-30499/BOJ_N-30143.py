def main():
    T = int(input())
    for _ in range(T):
        N, A, D = map(int, input().split())
        A_N = A + (N - 1) * D
        print((N * (A + A_N)) // 2)


if __name__ == "__main__":
    main()
