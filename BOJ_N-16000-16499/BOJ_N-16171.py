def main():
    S = input()
    K = input()

    text = ''.join([s for s in S if 65 <= ord(s) < 91 or 97 <= ord(s) < 123])
    print([0, 1][K in text])


if __name__ == "__main__":
    main()
