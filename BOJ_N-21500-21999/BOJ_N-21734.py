def main():
    text = input()
    for c in text:
        print(c * sum(map(int, str(ord(c)))))


if __name__ == "__main__":
    main()
