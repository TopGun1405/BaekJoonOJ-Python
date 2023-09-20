def main():
    A, B = map(int, input().split())
    print(2 * B + 1 if A > B else 2 * A - 1)


if __name__ == "__main__":
    main()
