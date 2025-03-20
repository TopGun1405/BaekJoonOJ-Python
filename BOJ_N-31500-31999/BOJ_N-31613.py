def main():
    X = int(input())
    N = int(input())

    cnt = 0
    while X < N:
        r = X % 3

        if r == 0:
            X += 1
        elif r == 1:
            X *= 2
        elif r == 2:
            X *= 3

        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
