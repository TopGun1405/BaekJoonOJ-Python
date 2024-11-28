def main():
    A, B = map(int, input().split())

    if not A % 2 and B % 2:
        print((B - A) // 2 + 2)
    else:
        print((B - A) // 2 + 1)


if __name__ == "__main__":
    main()
