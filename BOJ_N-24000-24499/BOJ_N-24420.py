def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    print(sum(A[1:-1]))


if __name__ == "__main__":
    main()
