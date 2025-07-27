def main():
    S = input()

    L = "qwertyasdfgzxcvb"
    R = "uiophjklnm"
    left, right, etc = 0, 0, 0
    for c in S:
        if c.isupper():
            etc += 1

    for c in S.lower():
        if c in L:
            left += 1
        elif c in R:
            right += 1
        else:
            etc += 1

    for _ in range(etc):
        if left <= right:
            left += 1
        else:
            right += 1

    print(left, right)


if __name__ == "__main__":
    main()
