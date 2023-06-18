def main():
    i = 0
    while True:
        try:
            _ = input()
            i += 1
        except EOFError:
            print(i)
            break


if __name__ == "__main__":
    main()
