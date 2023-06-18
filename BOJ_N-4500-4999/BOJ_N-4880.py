def main():
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        if b - a == c - b:
            print("AP {}".format(2 * c - b))
        elif b // a == c // b:
            print("GP {}".format(c ** 2 // b))


if __name__ == "__main__":
    main()
