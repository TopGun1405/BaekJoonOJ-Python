def main():
    while True:
        a, b, c, d = map(int, input().split())
        if a == b == c == d == 0:
            break
        print(c - b, d - a)


if __name__ == "__main__":
    main()
