def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    left, right = 0, 0
    while right < N:
        A_sum = sum(A[left:right+1])
        if A_sum > M:
            left += 1
        elif A_sum < M:
            right += 1
        else:
            cnt += 1
            right += 1

    print(cnt)


if __name__ == "__main__":
    main()
