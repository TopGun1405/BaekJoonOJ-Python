def main():
    hole = {
        'A': 1, 'a': 1, 'B': 2, 'b': 1, 'D': 1, 'd': 1, 'e': 1, 'g': 1,
        'O': 1, 'o': 1, 'P': 1, 'p': 1, 'Q': 1, 'q': 1, 'R': 1, '@': 1
    }

    S = input()
    cnt = 0
    for c in S:
        try:
            cnt += hole[c]
        except KeyError:
            continue

    print(cnt)


if __name__ == "__main__":
    main()
