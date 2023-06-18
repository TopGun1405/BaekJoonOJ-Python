def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    mult = 1
    for n in nums:
        mult *= n
    print(mult % M)


if __name__ == "__main__":
    main()
