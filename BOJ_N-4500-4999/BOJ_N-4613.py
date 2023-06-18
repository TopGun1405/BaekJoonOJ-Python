def main():
    while True:
        text = input()
        if text == '#':
            break
        QS = 0
        for i in range(len(text)):
            QS = QS if text[i] == ' ' else QS + (i + 1) * (ord(text[i]) - 64)
        print(QS)


if __name__ == "__main__":
    main()
