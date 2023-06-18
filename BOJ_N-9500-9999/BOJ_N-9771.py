def main():
    word, text = input(), ''
    while True:
        try:
            text += input()
        except EOFError:
            break
    print(text.count(word))


if __name__ == "__main__":
    main()
