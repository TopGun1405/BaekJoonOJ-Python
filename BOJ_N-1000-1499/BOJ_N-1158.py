def main():
    N, K = map(int, input().split())
    nums = list(range(1, N + 1))
    i, josephus = 0, []
    for _ in range(N):
        i += K - 1
        if i >= len(nums):
            i = i % len(nums)
        josephus.append(str(nums.pop(i)))
    print("<{}>".format(', '.join(josephus)))


if __name__ == "__main__":
    main()
