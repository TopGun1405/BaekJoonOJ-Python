def main():
    n = int(input())
    for _ in range(n):
        name = input()

        vowels = 0
        for c in name:
            if c in ["a", "e", "i", "o", "u"]:
                vowels += 1

        print(name)
        print(1 if vowels > len(name) / 2 else 0)


if __name__ == "__main__":
    main()
