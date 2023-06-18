def main():
    N = int(input())
    n = 0
    for _ in range(N):
        C, K = map(int, input().split())
        n += C * K
    print(n)


if __name__ == "__main__":
    main()
