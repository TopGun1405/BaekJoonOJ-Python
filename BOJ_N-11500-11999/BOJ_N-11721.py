def main():
    s = input()
    while True:
        if len(s) <= 10:
            print(s)
            break
        print(s[:10])
        s = s[10:]


if __name__ == "__main__":
    main()
