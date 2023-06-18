def main():
    A, B, C = map(int, input().split())
    time = [0] * 100
    p = 0
    for _ in range(3):
        begin, end = map(int, input().split())
        for i in range(begin, end):
            time[i] += 1
    for i in time:
        p += {0: 0, 1: A, 2: B * 2, 3: C * 3}[i]
    print(p)


if __name__ == "__main__":
    main()
