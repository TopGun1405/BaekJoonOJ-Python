def main():

    priority = {
        'lower': 0,
        'upper': 1,
        'digit': 2
    }

    def custom_key(char: str) -> tuple:
        if char.islower():
            cat = "lower"
        elif char.isupper():
            cat = "upper"
        elif char.isdigit():
            cat = "digit"
        else:
            cat = "other"

        return priority.get(cat, 99), char

    while True:
        S = input()

        if S == "#":
            break

        print("".join(sorted(S, key=custom_key)))


if __name__ == "__main__":
    main()
