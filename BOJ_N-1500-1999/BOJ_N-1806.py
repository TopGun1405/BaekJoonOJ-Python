def main():
    # incomplete
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    left, right = 0, 0
    tot, minLen = 0, int(1e9)
    while True:
        if tot >= S:
            minLen = min(minLen, right - left)
            tot -= A[left]
            left += 1
        elif right == N:
            break
        else:
            tot += A[right]
            right += 1

        if minLen == int(1e9):
            right += 1
        else:
            print(minLen)


if __name__ == "__main__":
    main()
