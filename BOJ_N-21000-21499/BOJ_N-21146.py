def main():
    n, k = map(int, input().split())
    maxSum = 0
    for _ in range(k):
        r = int(input())
        maxSum += r
    minSum, maxSum = maxSum - 3 * (n - k), maxSum + 3 * (n - k)
    print("{:.6f} {:.6f}".format(minSum / n, maxSum / n))


if __name__ == "__main__":
    main()
