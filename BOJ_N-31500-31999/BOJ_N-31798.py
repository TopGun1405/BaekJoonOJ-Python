def main():
    a, b, c = map(int, input().split())

    if a == 0:
        print(c**2 - b)
    elif b == 0:
        print(c**2 - a)
    elif c == 0:
        print(int((a + b)**0.5))


if __name__ == "__main__":
    main()
