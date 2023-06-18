def main():
    while True:
        text = input()
        if text == '#':
            break
        print(len(set(filter(lambda c: c.isalpha(), text.lower()))))


if __name__ == "__main__":
    main()
