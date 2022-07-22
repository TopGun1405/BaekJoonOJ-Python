def main():
    N, M = map(int, input().split())
    print(N // 2 if N < M else M // 2)


if __name__ == "__main__":
    main()
