def main():
    A, B, N = map(int, input().split())
    for n in range(N):
        print(A * N + B * (n + 1), end=' ')


if __name__ == "__main__":
    main()
