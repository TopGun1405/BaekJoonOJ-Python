def main():
    while True:
        try:
            S = input()
        except EOFError:
            break
        low, up, num, blank = 0, 0, 0, 0
        for s in S:
            if s.islower():
                low += 1
            elif s.isupper():
                up += 1
            elif s.isdigit():
                num += 1
            elif s == ' ':
                blank += 1
        print(low, up, num, blank)


if __name__ == "__main__":
    main()
