def main():
    N = int(input())
    liq = list(map(int, input().split()))

    low, high = 0, N - 1
    left, right = low, high
    merge = abs(liq[left] + liq[right])
    while low < high and merge != 0:
        val = liq[low] + liq[high]

        if abs(val) < merge:
            left, right = low, high
            merge = abs(val)

        if val < 0:
            low += 1
        else:
            high -= 1
    print(liq[left], liq[right])


if __name__ == "__main__":
    main()
