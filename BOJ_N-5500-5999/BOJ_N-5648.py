def main():
    n = input().split()

    n, nums = int(n[0]), list(map(lambda x: int(x[::-1]), n[1:]))
    while len(nums) < n:
        k = list(map(lambda x: int(x[::-1]), input().split()))
        nums += k

    print(*sorted(nums), sep="\n")


if __name__ == "__main__":
    main()
