def main():
    N = int(input())
    # A = list(map(lambda s: list(map(int, s.split())), input().split('-1')))
    # print(min(A[0]) + min(A[1]))
    A = list(map(int, input().split()))
    mid = A.index(-1)
    left, right = min(A[:mid]), min(A[mid + 1:])
    print(left + right)


if __name__ == "__main__":
    main()
