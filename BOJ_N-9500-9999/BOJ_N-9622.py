def main():
    t = int(input())

    cnt = 0
    for _ in range(t):
        length, width, depth, weight = map(float, input().split())
        if (length > 56 or width > 45 or depth > 25) and length + width + depth > 125 or weight > 7:
            print(0)
            continue
        print(1)
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
