def main():
    N = int(input())
    A = list(map(int, input().split()))

    # print(1 if len(A) == len(set(A)) else 0)
    prev = A[0]
    for i in range(1, N):
        if A[i] == prev:
            print(0)
            break
        prev = A[i]
    else:
        print(1)


if __name__ == "__main__":
    main()
