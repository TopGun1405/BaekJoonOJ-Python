def main():
    while True:
        try:
            A, B, C = map(int, input().split())
            print(max(B - A, C - B) - 1)
        except EOFError:
            break


if __name__ == "__main__":
    main()
