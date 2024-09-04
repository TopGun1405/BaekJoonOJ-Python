def main():
    N = int(input())
    H = [0] + [A-B for A, B in [map(int, input().split()) for _ in range(N)]]

    D = [0] * (N+1)
    for i in range(1, N+1):
        D[i] = D[i-1] + H[i]

    print(*D[1:], sep="\n")


if __name__ == "__main__":
    main()
