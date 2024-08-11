def main():
    N, M = map(int, input().split())
    if N == 0:
        print(0)
    else:
        books = list(map(int, input().split()))
        box, weight = 1, 0
        for book in books:
            if book + weight <= M:
                weight += book
            else:
                weight = book
                box += 1
        print(box)


if __name__ == "__main__":
    main()
