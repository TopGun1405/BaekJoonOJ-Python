def main():
    book = int(input())
    for _ in range(9):
        m = int(input())
        book -= m
    print(book)


if __name__ == "__main__":
    main()
