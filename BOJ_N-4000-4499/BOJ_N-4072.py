def main():
    while True:
        lines = input()
        if lines == "#":
            break
        print(" ".join(map(lambda w: w[::-1], lines.split())))


if __name__ == "__main__":
    main()
