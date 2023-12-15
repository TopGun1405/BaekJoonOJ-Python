def main():
    N, S = map(int, input().split())
    sizes = sorted([int(input()) for _ in range(N)])

    # pypy3
    # cnt = 0
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if sizes[i] + sizes[j] <= S:
    #             cnt += 1
    # print(cnt)

    cnt = 0
    low, high = 0, N-1
    while low < high:
        if sizes[low] + sizes[high] > S:
            high -= 1
        else:
            cnt += high - low
            low += 1
    print(cnt)


if __name__ == "__main__":
    main()
