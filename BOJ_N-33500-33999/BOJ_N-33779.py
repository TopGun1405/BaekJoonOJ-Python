def main():
    s = input()

    i = len(s) // 2

    print("beep" if s[:i] == s[i+(1 if len(s) % 2 else 0):][::-1] else "boop")


if __name__ == "__main__":
    main()
