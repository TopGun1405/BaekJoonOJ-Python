def main():
    s = input()

    idx = 0
    for i in range(len(s)):
        if s[i] in ["a", "e", "i", "o", "u"]:
            idx = i

    print(s[:idx+1] + "ntry")


if __name__ == "__main__":
    main()
