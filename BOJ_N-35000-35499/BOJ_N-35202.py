def main():
    c, n = map(int, input().split())

    if n < c:
        print(0)
    elif n > c:
        print(c + 1)
    else:
        print(c)


if __name__ == "__main__":
    main()
