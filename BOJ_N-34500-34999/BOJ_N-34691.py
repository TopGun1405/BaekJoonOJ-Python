def main():
    symbols = {
        'animal': "Panthera tigris",
        'tree': "Pinus densiflora",
        'flower': "Forsythia koreana"
    }
    while True:
        s = input()

        if s == "end":
            break

        print(symbols[s])


if __name__ == "__main__":
    main()
