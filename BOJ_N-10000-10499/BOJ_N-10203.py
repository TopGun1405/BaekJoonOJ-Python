def main():
    t = int(input())
    for _ in range(t):
        word = input()

        vowels = 0
        for c in word:
            if c in "aeiou":
                vowels += 1

        print(f"The number of vowels in {word} is {vowels}.")


if __name__ == "__main__":
    main()
