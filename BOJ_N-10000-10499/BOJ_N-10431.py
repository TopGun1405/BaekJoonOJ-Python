def main():
    P = int(input())
    for _ in range(P):
        heights = list(map(int, input().split()))
        T, heights = heights[0], heights[1:]
        step = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                if heights[i] > heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    step += 1
        print(T, step)


if __name__ == "__main__":
    main()
