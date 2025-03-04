def main():
    while True:
        N = int(input())

        if N == 0:
            break

        nums = set()
        for _ in range(N):
            tickets = set(map(int, input().split()))
            nums |= tickets

        print("Yes" if len(nums) == 49 else "No")


if __name__ == "__main__":
    main()
