def main():
    N = int(input())
    A = list(map(int, input().split()))
    i = A.index(max(A))
    print(sum(A[:i]))
    print(sum(A[i+1:]))


if __name__ == "__main__":
    main()
