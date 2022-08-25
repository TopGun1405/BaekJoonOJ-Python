def main():
    train, m = 0, 0
    for _ in range(4):
        o, i = map(int, input().split())
        train = train - o + i
        if train > m:
            m = train
    print(m)


if __name__ == "__main__":
    main()
