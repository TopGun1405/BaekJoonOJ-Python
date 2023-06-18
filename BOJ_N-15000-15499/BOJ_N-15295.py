def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        print(K, N * (N + 3) // 2)


if __name__ == "__main__":
    main()
