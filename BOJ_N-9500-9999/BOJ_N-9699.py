def main():
    T = int(input())
    for t in range(T):
        nums = list(map(int, input().split()))
        print("Case #{}: {}".format(t + 1, max(nums)))


if __name__ == "__main__":
    main()
