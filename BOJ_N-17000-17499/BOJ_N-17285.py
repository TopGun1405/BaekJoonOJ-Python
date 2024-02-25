def main():
    T = input()

    key = ord(T[0]) ^ ord("C")
    for c in T:
        print(chr(ord(c) ^ key), end="")


if __name__ == "__main__":
    main()
