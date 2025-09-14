def main():
    N, M, S = map(int, input().split())

    A = (M + 1) * S * (100 - N) // 100
    B = M * S

    print(min(A, B))


if __name__ == "__main__":
    main()
