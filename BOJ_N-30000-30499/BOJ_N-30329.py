def main():
    s = input()
    kick = 0
    for i in range(len(s)):
        if s[i:i+4] == "kick":
            kick += 1
    print(kick)


if __name__ == "__main__":
    main()
