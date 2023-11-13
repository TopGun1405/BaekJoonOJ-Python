def main():
    N = int(input())
    results = [list(map(int, input().split())) for _ in range(N)]
    results.sort()
    for result in results:
        print(*result)


if __name__ == "__main__":
    main()
