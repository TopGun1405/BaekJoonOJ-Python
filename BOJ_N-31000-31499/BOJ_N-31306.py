def main():
    w = input()
    vowels, y = 0, 0
    for c in w:
        if c in ["a", "e", "i", "o", "u"]:
            vowels += 1
        elif c == "y":
            y += 1
    print(vowels, vowels + y)


if __name__ == "__main__":
    main()
