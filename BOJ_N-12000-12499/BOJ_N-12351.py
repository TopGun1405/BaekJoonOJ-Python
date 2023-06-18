def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        height = list(map(int, input().split()))
        for i in range(1, N - 1):
            avg = (height[i - 1] + height[i + 1]) / 2
            if height[i] > avg:
                height[i] = avg
        print("Case #{}: {:0.7f}".format(t + 1, height[N - 2]))


if __name__ == "__main__":
    main()
