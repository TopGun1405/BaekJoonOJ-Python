def main():
    n = int(input())
    gravel = list(map(int, input().split()))

    left, right = gravel[0], gravel[1]
    for i in range(2, n):
        if left == right:
            left += gravel[i]
        elif left > right:
            right += gravel[i]
        else:
            left += gravel[i]

    diff = abs(right - left)
    if diff == 0:
        print(0)
    else:
        cnt = 0
        for weight in [100, 50, 20, 10, 5, 2, 1]:
            if diff // weight != 0:
                cnt += diff // weight
                diff %= weight

        print(cnt)


if __name__ == "__main__":
    main()
