def main():
    N, k = int(input()), int(input())
    low, high = 1, N * N
    while low <= high:
        mid = (low + high) // 2
        num = 0
        for i in range(1, N + 1):
            num += min((mid - 1) // i, N)
            print((mid - 1) // i, N)
        if num >= k:
            high = mid - 1
        elif num < k:
            low = mid + 1
    print(high)


if __name__ == "__main__":
    main()
