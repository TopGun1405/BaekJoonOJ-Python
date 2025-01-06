def main():
    i = 1
    while True:
        text = input()

        if text == "Was it a cat I saw?":
            break

        print(text[::i+1])
        i += 1


if __name__ == "__main__":
    main()
