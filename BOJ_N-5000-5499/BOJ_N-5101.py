def main():
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        print('X' if (c - a) % b or (c - a) // b + 1 <= 0 else (c - a) // b + 1)


if __name__ == "__main__":
    main()
