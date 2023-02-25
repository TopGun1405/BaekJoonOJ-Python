def main():
    text = [input().strip() for _ in range(5)]
    for i in range(15):
        for j in range(5):
            try:
                print(text[j][i], end='')
            except IndexError:
                continue


if __name__ == "__main__":
    main()
