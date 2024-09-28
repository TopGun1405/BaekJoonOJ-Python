def main():
    S = input()

    latest = ""
    for c in S:
        if latest != c:
            latest = c
            print(c, end="")


if __name__ == "__main__":
    main()
