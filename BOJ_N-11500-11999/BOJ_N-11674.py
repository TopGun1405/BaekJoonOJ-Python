def main():
    s = input()

    lv, x, y = len(s), 0, 0
    for l, c in enumerate(s):
        scale = lv-l-1
        if c == "1":
            x += 2 ** scale
        elif c == "2":
            y += 2 ** scale
        elif c == "3":
            x += 2 ** scale
            y += 2 ** scale

    print(lv, x, y)


if __name__ == "__main__":
    main()
