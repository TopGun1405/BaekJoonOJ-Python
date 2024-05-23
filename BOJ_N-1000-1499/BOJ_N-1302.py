def main():
    N = int(input())
    books = [input() for _ in range(N)]

    booksNum = {}
    for book in books:
        if booksNum.get(book, 0):
            booksNum[book] += 1
        else:
            booksNum[book] = 1

    booksNum = sorted(booksNum.items(), key=lambda k: (-k[1], k[0]))
    print(booksNum[0][0])


if __name__ == "__main__":
    main()
