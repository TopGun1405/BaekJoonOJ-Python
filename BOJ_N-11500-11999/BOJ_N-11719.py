def main():
    while True:
        try:
            s = input()
            print(s)
        except EOFError:
            break


if __name__ == "__main__":
    main()
