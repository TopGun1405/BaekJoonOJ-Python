def main():
    J, N = map(int, input().split())

    cnt = 0
    for _ in range(N):
        p = input()

        size = 0
        for c in p:
            if c.isupper():
                size += 4
            elif c.islower() or c.isdigit():
                size += 2
            elif c == " ":
                size += 1

        if size <= J:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
