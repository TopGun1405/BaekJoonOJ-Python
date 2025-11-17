def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    print("DIMI" if sum(A) - N >= M else "OUT")


if __name__ == "__main__":
    main()
