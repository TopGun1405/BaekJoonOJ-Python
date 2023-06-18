def main():
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    print(cutTree(tree, M))


def cutTree(tree, M):
    low, high = 0, max(tree)
    while True:
        mid = (low + high) // 2

        left = 0
        for height in tree:
            if height > mid:
                left += height - mid

        if left == M or low > high:
            return mid
        elif left > M:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    main()
