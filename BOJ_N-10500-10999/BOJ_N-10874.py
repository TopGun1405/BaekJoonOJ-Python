def main():
    N = int(input())
    for _ in range(N):
        nums = list(map(int, input().split()))
        cnt = 0
        for i in range(10):
            if nums[i] == (i + 1) % 5:
                cnt += 1
        if cnt == 8:
            print(_ + 1)


if __name__ == "__main__":
    main()
