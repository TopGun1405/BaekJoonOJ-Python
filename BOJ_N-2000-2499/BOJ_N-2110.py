def main():
    N, C = map(int, input().split())
    x = sorted([int(input()) for _ in range(N)])
    print(x)
    low, high = x[1] - x[0], x[-1] - x[0]
    print(low, high)
    while True:
        mid = (low + high) // 2
        break


if __name__ == "__main__":
    main()
