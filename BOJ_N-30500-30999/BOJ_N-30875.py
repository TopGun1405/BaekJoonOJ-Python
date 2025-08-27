def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N+1):
        print(*list(range(1, N+1)))


if __name__ == "__main__":
    main()
