def main():
    while True:
        text = input()
        if text == '*':
            break
        fanGram = set(list(''.join(text.split())))
        print(['N', 'Y'][len(fanGram) == 26])


if __name__ == "__main__":
    main()
