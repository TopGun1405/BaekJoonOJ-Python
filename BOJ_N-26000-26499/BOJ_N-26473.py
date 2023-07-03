def main():
    while True:
        N = int(input())
        if N == 0:
            break
        a = sorted(map(int, input().split()))

        length, current = [1], a[0]
        for ai in a[1:]:
            if ai - current == 1:
                length[-1] += 1
            else:
                length.append(1)
            current = ai
        print(max(length))


if __name__ == "__main__":
    main()
