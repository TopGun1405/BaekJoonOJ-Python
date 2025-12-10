def main():
    S = input()
    for i in range(26):
        print("".join(map(lambda c: chr((ord(c)-i+(26 if ord(c)-i < 65 else 0))), S)))


if __name__ == "__main__":
    main()
