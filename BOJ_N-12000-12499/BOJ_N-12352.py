def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        heights = list(map(int, input().split()))
        for i in range(1, N - 1):
            heights[i] = min(heights[i], (heights[i-1] + heights[i+1]) / 2)
        print(f"Case #{t}: {heights[N - 2]}")


if __name__ == "__main__":
    main()
