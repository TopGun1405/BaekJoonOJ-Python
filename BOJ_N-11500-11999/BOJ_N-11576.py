def main():
    A, B = map(int, input().split())
    m = int(input())
    nums = list(map(int, input().split()))[::-1]

    ten = 0
    for i, num in enumerate(nums):
        ten += num * (A ** i)

    res = []
    while ten // B:
        res.append(ten % B)
        ten //= B
    res.append(ten)

    print(*res[::-1])


if __name__ == "__main__":
    main()
