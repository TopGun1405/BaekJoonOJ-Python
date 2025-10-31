def main():
    card = input()

    tot = 0
    for i in range(len(card)-1, -1, -1):
        if i % 2:
            tot += int(card[i])
        else:
            tot += sum(map(int, str(int(card[i]) * 2)))

    print("DA" if tot % 10 == 0 else "NE")


if __name__ == "__main__":
    main()
