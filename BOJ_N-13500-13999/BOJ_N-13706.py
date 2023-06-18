def main():
    N = int(input())
    low = 1
    high = N

    # binary search
    while True:
        mid = (low + high) // 2
        if mid ** 2 == N:
            print(mid)
            break
        elif mid ** 2 > N:
            high = mid - 1
        elif mid ** 2 < N:
            low = mid + 1


if __name__ == "__main__":
    main()
