def main():
    while True:
        heights = list(map(int, input().split()))

        n, heights = heights[0], heights[1:]
        if n == 0:
            break

        stack = []
        maxVal, leftIdx = 0, 0
        for idx, height in enumerate(heights):
            leftIdx = idx
            while stack and stack[-1][1] > height:
                leftIdx, h = stack.pop()
                maxVal = max(maxVal, (idx - leftIdx) * h)
            stack.append([leftIdx, height])

        while stack:
            leftIdx, h = stack.pop()
            maxVal = max(maxVal, (len(heights) - leftIdx) * h)

        print(maxVal)


if __name__ == "__main__":
    main()
