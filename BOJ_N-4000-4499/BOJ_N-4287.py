def main():
    while True:
        words = input()

        if words == "#":
            break

        words = words.split()
        ans = ""
        for c1, c2, c3 in zip(words[0], words[1], words[2]):
            ans += chr(97 + ((ord(c3) + ord(c2) - ord(c1) - 97) % 26))

        print(" ".join(words) + " " + ans)


if __name__ == "__main__":
    main()
