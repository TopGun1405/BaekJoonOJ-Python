def main():
    K = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    cnt = 0
    for A_N in A:
        for B_N in B:
            if A_N + K == B_N:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
