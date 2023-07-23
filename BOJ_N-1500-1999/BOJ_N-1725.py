def main():
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    # heights = [int(input()) for _ in range(N)] + [0]

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
        maxVal = max(maxVal, (N - leftIdx) * h)

    print(maxVal)


if __name__ == "__main__":
    main()
