def main():
    nums = list(map(int, input().split()))

    last_pos = [0] * 11
    pos = {}
    for idx, num in enumerate(nums):
        pos[num] = idx

    for p in range(1, 11):
        sheet = [x for x in range(1, 101) if x % 10 == p % 10]
        last_pos[p] = max(pos[x] for x in sheet)

    print(max(range(1, 11), key=lambda i: last_pos[i]))


if __name__ == "__main__":
    main()
