def main():
    N = int(input())
    cnt = 0

    # Case 1: a = 0
    cnt += (2 * N + 1) ** 2

    # Case 2: a + b + c = 1
    # for a in range(-N, N + 1):
    #     if a == 0:
    #         continue
    #     for b in range(-N, N + 1):
    #         c = 1 - a - b
    #         if -N <= c <= N:
    #             cnt += 1
    for a in range(-N, N + 1):
        if a == 0:
            continue
        low = max(-N, 1 - a - N)
        high = min(N, 1 - a + N)
        if low <= high:
            cnt += (high - low + 1)

    print(cnt)


if __name__ == "__main__":
    main()
