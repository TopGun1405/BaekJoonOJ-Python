def main():
    ch = input()
    tot = 0
    for c in ch:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            tot += 1
    print(tot)


if __name__ == "__main__":
    main()
