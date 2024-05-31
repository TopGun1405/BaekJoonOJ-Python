def main():
    N = int(input())

    dictionary = {}
    for _ in range(N):
        text = input()
        for c in text:
            if c == " ":
                continue
            try:
                dictionary[c] += 1
            except KeyError:
                dictionary[c] = 1

    dictionary = sorted(dictionary.items())
    for order in dictionary:
        print(*order)


if __name__ == "__main__":
    main()
