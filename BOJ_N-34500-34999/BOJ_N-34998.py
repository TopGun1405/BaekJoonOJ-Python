def main():
    N = int(input())
    for _ in range(N):
        X = int(input())
        nums = "".join(input().split()).split("+")
        nums = list(map(lambda e: int(e) if e.isdigit() else e, nums))

        try:
            print(sum(nums) if sum(nums) < 10 else "!")
        except TypeError:
            print("!")


if __name__ == "__main__":
    main()
