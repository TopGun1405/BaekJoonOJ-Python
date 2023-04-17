def main():
    exp = input().split('-')
    nums = [sum(map(int, e.split('+'))) for e in exp]
    k = nums.pop(0)
    for n in nums:
        k -= n
    print(k)


if __name__ == "__main__":
    main()
